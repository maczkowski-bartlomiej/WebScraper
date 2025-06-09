from flask import Flask, request, render_template
import requests

app = Flask(__name__)
ENGINE_API = 'http://engine:8000'

def make_engine_request(method, endpoint, json=None):
    try:
        response = requests.request(method, f'{ENGINE_API}/{endpoint}', json=json)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error contacting engine: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            urls = request.form['urls'].split(',')
            data = make_engine_request('POST', 'tasks', json={'urls': urls})
            task_id = data['task_id']
            return render_template('result.html', task_id=task_id)
        except Exception as e:
            return str(e), 500
    return render_template('index.html')

@app.route('/data/<task_id>')
def get_data(task_id):
    try:
        data = make_engine_request('GET', f'data/{task_id}')
        return render_template('data.html', data=data['data'], task_id=task_id)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)