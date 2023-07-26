import elasticsearch


def main():
    es = elasticsearch.Elasticsearch([{'host':'localhost','port':9200}])
    es.delete(index='my_index1',id=1)

if __name__ == '__main__':
    main()