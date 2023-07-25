import mysql.connector
import pymysql


def update():
    try:
         db = pymysql.Connection(
             host="localhost",
             user="root",
             password="",
             port=3306,
             database="test"
         )
         cursor = db.cursor()
         sql = 'UPDATE EMPLOYEE SET AGE = 20 where FIRST_NAME = "sun"'
         cursor.execute(sql)
         db.commit()
    except Exception as e:
        db.rollback()
        print("Exception",e)

def main():
    update()

if __name__ == '__main__':
    main()