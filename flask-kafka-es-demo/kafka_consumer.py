from kafka import KafkaConsumer
from es_client import write_to_es
from config_loader import load_config
import json

cfg = load_config()

consumer = KafkaConsumer(
    cfg['kafka']['topic'],
    bootstrap_servers=cfg['kafka']['bootstrap_servers'],
    auto_offset_reset='earliest',
    group_id=cfg['kafka']['group_id'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    print(f"Consumed: {message.value}")
    write_to_es(message.value)
