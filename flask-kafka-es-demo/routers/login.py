

from flask import Blueprint, request, jsonify
from kafka_producer import send_to_kafka
import datetime

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def log_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['index'] = 'log-login'  # 💡 明确 index
    send_to_kafka(data)
    return jsonify({"message": "login success"}), 200
