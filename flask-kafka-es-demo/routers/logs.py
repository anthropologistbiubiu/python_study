

from flask import Blueprint, request, jsonify
from kafka_producer import send_to_kafka
import datetime

log_bp = Blueprint('log', __name__)


@log_bp.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['index'] = 'log-index'  # 💡 明确 index
    send_to_kafka(data)
    return jsonify({"message": "log received"}), 200


default_bp = Blueprint('default', __name__)


@default_bp.route('/default', methods=['POST'])
def log_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    data['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['index'] = 'log-default'  # 💡 明确 index
    send_to_kafka(data)
    return jsonify({"message": "log received"}), 200
