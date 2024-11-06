from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Base URL of your Django API
API_BASE_URL = "http://127.0.0.1:8000/api/properties/"

@app.route('/')
def property_list():
    response = requests.get(API_BASE_URL)
    properties = response.json() if response.status_code == 200 else []
    return render_template('property_list.html', properties=properties)

@app.route('/property/<int:property_id>')
def property_detail(property_id):
    response = requests.get(f"{API_BASE_URL}{property_id}/")
    property_data = response.json() if response.status_code == 200 else None
    return render_template('property_detail.html', property=property_data)

if __name__ == '__main__':
    app.run(debug=True)
