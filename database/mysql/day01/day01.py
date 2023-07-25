import pymysql




def connect_mysql():
    address = "127.0.0.1"
    port = 3306
    db = pymysql.connect(
        host=address,  # 填写数据库的主机IP地址
        user='root',  # 数据库用户名
        password='',  # 数据库密码
        port=port,  # 数据库端口号
        database='test',  # 数据库的名称
    )
    cursor = db.cursor()
    print(cursor)
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 创建数据表SQL语句
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""

    cursor.execute(sql)
    pass

def insert():
    # SQL 插入语句
    address = "127.0.0.1"
    port = 3306
    db = pymysql.connect(
        host=address,  # 填写数据库的主机IP地址
        user='root',  # 数据库用户名
        password='',  # 数据库密码
        port=port,  # 数据库端口号
        database='test',  # 数据库的名称
    )
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    pass

def drop():
    pass
def update():
    pass


def query():
    pass

def main():
    connect_mysql()
    pass

if __name__ == '__main__':
    main()