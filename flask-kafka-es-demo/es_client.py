

from elasticsearch import Elasticsearch
from config_loader import load_config

cfg = load_config()
es = Elasticsearch(cfg['elasticsearch']['host'])


def write_to_es(doc, index):
    es.index(index=index, document=doc)
