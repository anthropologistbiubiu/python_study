import pymongo





def main():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['test']
    collections = db.list_collection_names()
    print(collections)
    collection = db['student']
    cursor = collection.find()
    for doc in cursor:
        print(doc)


if __name__ == '__main__':
    main()