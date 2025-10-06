from flask import Flask, request, jsonify
from kafka_producer import send_to_kafka

app = Flask(__name__)


@app.route('/log', methods=['POST'])
def handle_log():
    data = request.get_json()
    send_to_kafka(data)
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
