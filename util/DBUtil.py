import pymysql


# 帮助类

class DbUtil:
    conn: object
    cursor: object

    def __init__(self):
        # 开启连接 得到游标对象
        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='124578',
                                    database='数据库实验', charset='utf8')
        self.cursor = self.conn.cursor()

    def execute(self, sql: str, val: tuple = None):
        self.cursor.execute(sql, val)
        self.conn.commit()

    def execute_list(self, sql: str):
        self.cursor.execute(sql, None)
        self.conn.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

