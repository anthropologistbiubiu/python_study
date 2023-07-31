




def establish():
    import pymongo
    # 连接到MongoDB服务器
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # 指定数据库
    db = client["mydatabase"]
    # 指定集合（相当于关系数据库中的表）
    collection = db["mycollection"]
    # 插入一条数据
    data = {"name": "John", "age": 30, "email": "john@example.com"}
    collection.insert_one(data)

def main():
    establish()


if __name__ == '__main__':
    main()