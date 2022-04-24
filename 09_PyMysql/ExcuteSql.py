import pymysql
import DBExcute
from DBExcute import DBTools

# 查询语句
# sqlSel="select * from t_book"
# DBTools.excuteSql(sqlSel)

# 删除语句
sqlDelte = "update t_book set `title`='元气囡仔' where id=5;"
result = DBTools.excuteSql(sqlDelte)
print(result)
