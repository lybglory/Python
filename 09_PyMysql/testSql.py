# 导入封装好的数据库操作类.py文件
import  DBTools
# 导入py文件里的DBTools类
from DBTools import DBTools

# 查询语句
# sql="select * from t_book"

# 更新语句
sql= "update t_book set `title`='加油吧！' where id=5;"
result = DBTools.executeSQL(sql)
print(result)
# 有1条数据受影响
# 1