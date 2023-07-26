

from elasticsearch import Elasticsearch

# 连接到本地的Elasticsearch节点


def main():
    try:
        es = Elasticsearch([{"host":"localhost","port":"9200"}])
        print(es.ping())
    except Exception as e:
        print("Exception",e)
    if es.ping():
        doc = {
            'title': 'Python Elasticsearch Tutorial',
            'content': 'Elasticsearch is a powerful search engine and analytics engine.',
        }
        # 创建一个新的索引并插入文档
        res = es.index(index='my_index', doc_type='my_type', id=1, body=doc)
        print(res['result'])  # 输出：created


if __name__ == '__main__':
    main()