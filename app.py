from flask import Flask, render_template, jsonify
import json
import requests
from threading import Timer
from requests.auth import HTTPBasicAuth
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

products = []

def load_products():
    global products
    try:
        response = requests.get(app.config['API_URL'], auth=HTTPBasicAuth(app.config['API_USERNAME'], app.config['API_PASSWORD']))
        if response.status_code == 200:
            products = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

def update_products():
    load_products()
    Timer(30, update_products).start()

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/api/products')
def api_products():
    return jsonify(products)

if __name__ == '__main__':
    load_products()
    update_products()
    app.run(debug=True, port=5000)  # Port 5000
