import pymongo


# 删除数据

def delete_one():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['test']
    collection = db['student']
    query = {'name':'yujinling'}
    collection.delete_one(query)
    cursor = collection.find()
    for doc in cursor:
        print(doc)


if __name__ == '__main__':
    delete_one()