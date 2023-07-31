import pymongo


def query():
    # 查询集合中所有数据
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['mydatabase']
    print(db)
    collection = db['mycollection']
    all_data = collection.find()
    print(all_data)
    # 查询年龄大于等于25的数据
    query = {"age": {"$gte": 25}}
    result = collection.find(query)
    for data in result:
        print(data)


def main():
    query()


if __name__ == '__main__':
    main()