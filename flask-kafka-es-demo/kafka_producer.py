
from kafka import KafkaProducer
import json
from config_loader import load_config

cfg = load_config()
producer = KafkaProducer(
    bootstrap_servers=cfg['kafka']['bootstrap_servers'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_to_kafka(data):
    producer.send(cfg['kafka']['topic'], data)
    producer.flush()
