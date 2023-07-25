import pymysql





def insert():
    try:
        db = pymysql.connect(host="127.0.0.1",user="root",password="",port=3306,database="test")
        cursor = db.cursor()
        sql = 'INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX)VALUES("sun","weiming",18,"m")'
        cursor.execute(sql)
    except Exception as e:
        print("Exception ",e)


def main():
    insert()


if __name__ == '__main__':
    main()