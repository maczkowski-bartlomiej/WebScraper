FROM python:3.13.3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "scraping_engine:app", "--host", "0.0.0.0", "--port", "8000"]