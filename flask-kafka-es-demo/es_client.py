

from elasticsearch import Elasticsearch
from config_loader import load_config
from datetime import datetime

cfg = load_config()
es = Elasticsearch(cfg['elasticsearch']['host'])


def write_to_es(doc):
    doc["timestamp"] = datetime.utcnow().isoformat()
    es.index(index=cfg['elasticsearch']['index'], document=doc)
