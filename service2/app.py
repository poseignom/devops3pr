from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Service 2",
        "status": "running",
        "message": "Hello from Service 2!"
    })

@app.route('/info')
def info():
    return jsonify({
        "data": "Information from Service 2",
        "timestamp": "2024-01-15T12:00:00Z"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)