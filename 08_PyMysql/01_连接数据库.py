# 导包
import pymysql

# 创建链接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="root",
                       database="books")

# 获取游标
cursor = conn.cursor()

# 执行sql
sql = "select * from t_book"
cursor.execute(sql)
print(cursor.fetchall())

# 关闭游标
cursor.close()

# 关闭连接
conn.close()