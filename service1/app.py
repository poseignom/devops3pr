from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Service 1",
        "status": "running",
        "message": "Hello from Service 1!"
    })

@app.route('/data')
def get_data():
    # Пример общения со вторым сервисом
    try:
        response = requests.get('http://service2:5001/info')
        return jsonify({
            "service1_data": "Data from service 1",
            "service2_response": response.json()
        })
    except:
        return jsonify({"error": "Cannot connect to service2"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)