import pymysql


def delete():
    try:
        db = pymysql.Connection(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="test"
        )
        cursor = db.cursor()
        sql = "DELETE FROM EMPLOYEE WHERE AGE > 10"
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("Exception",e)
    finally:
        cursor.close()
        db.close()
def main():
    delete()

if __name__ == '__main__':
    main()