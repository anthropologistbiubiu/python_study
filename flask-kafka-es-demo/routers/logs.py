from flask import Blueprint, request, jsonify
from kafka_producer import send_to_kafka
import datetime

logs_bp = Blueprint('logs', __name__)


@logs_bp.route('/in', methods=['POST'])
def login_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['index'] = 'log-login'  # 💡 明确 index
    send_to_kafka(data)
    return jsonify({"message": "login success"}), 200


@logs_bp.route('/out', methods=['POST'])
def logout_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['index'] = 'log-out'  # 💡 明确 index
    send_to_kafka(data)
    return jsonify({"message": "logout success"}), 200
