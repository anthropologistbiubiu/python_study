

from elasticsearch import Elasticsearch

# 连接到本地的Elasticsearch节点
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 创建一个新的索引并插入文档
doc = {
    'title': 'Python Elasticsearch Tutorial',
    'content': 'Elasticsearch is a powerful search engine and analytics engine.',
}
res = es.index(index='my_index', doc_type='my_type', id=1, body=doc)
print(res['result'])  # 输出：created
