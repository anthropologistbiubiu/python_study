import pymongo







def main():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    dbs = client.list_database_names()
    print(dbs)


if __name__ == '__main__':
    main()