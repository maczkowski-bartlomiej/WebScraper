import asyncio
import aiohttp
from bs4 import BeautifulSoup
from multiprocessing import Pool
import motor.motor_asyncio
import re
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from bson import ObjectId
from urllib.parse import urlparse

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://21262:21262@cluster.tjmkkiz.mongodb.net/?retryWrites=true&w=majority&appName=cluster')
db = client.scraped_data

def count_tags(soup):
    tag_counts = {}
    for tag in soup.find_all():
        tag_name = tag.name
        tag_counts[tag_name] = tag_counts.get(tag_name, 0) + 1
    return tag_counts

def count_internal_links(soup, base_url):
    parsed_base = urlparse(base_url)
    base_domain = parsed_base.netloc
    internal_links = 0
    for a in soup.find_all('a', href=True):
        href = a['href']
        parsed_href = urlparse(href)
        if parsed_href.netloc == base_domain or not parsed_href.netloc:
            internal_links += 1
    return internal_links

def extract_data(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    tag_counts = count_tags(soup)
    org_structure = [tag.text.strip() for tag in soup.find_all(['h1', 'h2', 'h3'])]
    internal_links = count_internal_links(soup, base_url)
    page_title = soup.title.string if soup.title else "No title found"
    return {
        'emails': emails,
        'tag_counts': tag_counts,
        'org_structure': org_structure,
        'internal_links': internal_links,
        'page_title': page_title
    }

async def store_scraped_data(urls, results, task_id):
    for url, data in zip(urls, results):
        await db.data.insert_one({
            'task_id': task_id,
            'url': url,
            'emails': data['emails'],
            'tag_counts': data['tag_counts'],
            'org_structure': data['org_structure'],
            'internal_links': data['internal_links'],
            'page_title': data['page_title']
        })
    await db.tasks.update_one({'task_id': task_id}, {'$set': {'status': 'completed'}}, upsert=True)

async def scrape_urls(urls, task_id):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        html_contents = [await response.text() for response in responses]
    with Pool() as pool:
        results = pool.starmap(extract_data, [(html, url) for html, url in zip(html_contents, urls)])
    await store_scraped_data(urls, results, task_id)

app = FastAPI()

class ScrapeRequest(BaseModel):
    urls: list[str]

@app.post('/tasks')
async def create_task(request: ScrapeRequest, background_tasks: BackgroundTasks):
    task_id = str(hash(''.join(request.urls)))
    await db.tasks.insert_one({'task_id': task_id, 'status': 'pending', 'urls': request.urls})
    background_tasks.add_task(scrape_urls, request.urls, task_id)
    return {'task_id': task_id}

@app.get('/data/{task_id}')
async def get_data(task_id: str):
    data = await db.data.find({'task_id': task_id}).to_list(length=100)
    for item in data:
        if '_id' in item:
            item['_id'] = str(item['_id'])
    return {'data': data}