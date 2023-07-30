

# 明天早上完成 es 的搜索，精准匹配，模糊匹配。

'''
查询数据
查询结果返回参数各字段含义
最直接的查询方法
用body指定条件
模糊查询
term 精确查询
multi_match，多字段查询
prefix，前缀查询
wildcard，通配符查询
regexp，正则匹配
bool，多条件查询
'''
import elasticsearch


# 用body指定条件
def body_search():
    es = elasticsearch.Elasticsearch([{'host':'localhost','port':9200}])
    body = {
       'from' :0,
        'size' :10
    }
    print(es.search(index='my_index',body=body))




def main():
    body_search()


if __name__ == '__main__':
    main()
