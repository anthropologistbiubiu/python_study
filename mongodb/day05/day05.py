import pymongo





def main():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['test']
    collection = db['student']
    query = {'name':'yujinling'}
    new_data = {'$set':{'age':10}}
    collection.update_one(query,new_data)
    cursor = collection.find()
    for doc in cursor:
        print(doc)
def update_many():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['test']
    collection = db['student']
    query = {'name':'yujinling'}
    new_data = {'$set':{'age':10}}
    collection.update_many(query,new_data)
    cursor = collection.find()
    for doc in cursor:
        print(doc)

if __name__ == '__main__':
    update_many()