from kafka import KafkaConsumer
import json
from config_loader import load_config
from es_client import write_to_es

cfg = load_config()

consumer = KafkaConsumer(
    cfg['kafka']['topic'],
    bootstrap_servers=cfg['kafka']['bootstrap_servers'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='log-consumer-group'
)

print("Consumer started...")

for message in consumer:
    data = message.value
    index = data.pop("index", "log-default")  # 如果没传 index 用默认
    write_to_es(data, index=index)
