# 导入PyMysql
import pymysql

# 1、连接数据库
conn =pymysql.connect(host="localhost",
                      port=3306,
                      user="root",
                      password="root",
                      database="books")
# 2、获取游标
cur = conn.cursor()

# 3、执行sql
sql = "select * from t_book"
cur.execute(sql)
# 获取查询结果的总记录数
print("查询结果总记录数=%d,游标位置=%d" %(cur.rowcount,cur.rownumber))
print("-"*20)

print(cur.fetchone())
print("查询结果总记录数=%d,游标位置=%d" %(cur.rowcount,cur.rownumber))

# 游标置0
# cur.rownumber = 0
print(cur.fetchall())

# 4、关闭游标
cur.close()

# 5、关闭连接
conn.close()

