# 1、导包
import pymysql


class DBTools:
    __conn = None  # 私有属性，连接对象
    __cur = None  # 私有属性，游标

    # 2、封装连接数据库，私有类方法
    @classmethod
    def __getConn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="localhost",
                                         port=3306, user="root",
                                         password="root",
                                         database="books")
        return cls.__conn

    # 3、封装获取游标，私有类方法
    @classmethod
    def __getCur(cls):
        if cls.__cur is None:
            cls.__cur = cls.__getConn().cursor()
        return cls.__cur

    # 4、公开类方法，执行SQL语句，传入sql语句参数
    @classmethod
    def excuteSql(cls, strSql):
        try:
            # 1、获取游标的时候，就会调用创建连接对象
            cls.__cur = cls.__getCur()
            cls.__cur.execute(strSql)
            # 如果是查询语句，返回结果
            if (strSql.split(" ")[0]) == "select":
                print(cls.__cur.fetchall())
                return cls.__cur.fetchall()
            else:
                # 否则提交数据
                cls.__conn.commit()
                # rowcount表示总行数
                # rownumber表示游标当前的位置
                print("有%d条数据受到影响" % cls.__cur.rowcount)
                return cls.__cur.rowcount
        except Exception as result:
            # sql语句出现异常处理，回滚
            cls.__conn.rollback()
            print(result)
        finally:
            cls.__closeCur()  # 关闭游标
            cls.__closeConn()  # 关闭连接

    # 私有类方法，封装关闭游标
    @classmethod
    def __closeCur(cls):
        if cls.__cur:
            cls.__cur.close()
            cls.__cur = None

    # 私有类方法，封装关闭连接对象
    @classmethod
    def __closeConn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None
