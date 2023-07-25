import pymysql


def query():
    try:
        db = pymysql.Connection(host="localhost",user="root",password='',port=3306,database="test")
        cursor = db.cursor()
    except Exception as e:
        print("Exception",e)
    try:
        sql = 'SELECT * FROM EMPLOYEE'
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        db.commit()
    except Exception as e:
        try:
            db.rollback()
        except Exception as e:
           print("Exception ",e)
        print("Exception",e)

def main():
    query()
    pass


if __name__ == '__main__':
    main()