# 导包
import pymysql

# 1、创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="root",
                       database="books",
                       autocommit=True)

# 2、获取游标
cur = conn.cursor()

# 3、执行SQL
sql="update t_book set  title='白色巨塔',`read`=95680 where id=5;"
print("受影响的行数=%d,游标位置=%d" %(cur.rowcount,cur.rownumber))
# 受影响的行数=-1,游标位置=0

cur.execute(sql)
print("受影响的行数=%d,游标位置=%d" %(cur.rowcount,cur.rownumber))
# 受影响的行数=1,游标位置=0

# 4、关闭游标
cur.close()

# 5、关闭连接
conn.close()