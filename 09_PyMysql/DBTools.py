import pymysql

class DBTools:
    __conn = None  # 私有属性，连接数据库对象
    __cur = None  # 私有属性，游标对象

    # 私有类方法，封装数据库连接方法
    @classmethod
    def __getConn(cls):
        cls.__conn = pymysql.connect(
            host="localhost", port=3306,
            user="root", password="root",
            database="books"
                                     )
        return cls.__conn

    # 私有类方法，封装获取游标对象的方法
    @classmethod
    def __getCur(cls):
        if cls.__cur is None:
            # 获取连接对象并创建游标对象
            cls.__cur = cls.__getConn().cursor()
        return cls.__cur

    # 对外公共的方法，封装执行SQL语句
    @classmethod
    def executeSQL(cls, sql):
        # 外界调用，传入sql语句即可
        try:
            # 1、首先连接数据，获取数据库连接对象
            # 2、调用获取游标对象的方法
            #   获取游标方法已经调用了获取数据库连接的方法
            cls.__cur = cls.__getCur()

            # 3、执行SQL语句
            cls.__cur.execute(sql)
            # 判断sql语句是查询语句还是非查询语句

            if (sql.split(" ")[0]).lower() == "select":
                return cls.__cur.fetchall()
            else:
                # 连接对象提交事务
                cls.__conn.commit()
                print("有%d条数据受影响" % (cls.__cur.rowcount))
                return cls.__cur.rowcount
        except Exception as result:
            # 连接对象回滚事务，抛出异常
            cls.__conn.rollback()
            print(result)
        finally:
            # 无论是否有异常，调用关闭对象、游标的方法
            cls.__closeCur()
            cls.__closeConn()

    # 私有类方法，封装关闭游标对象的方法
    @classmethod
    def __closeCur(cls):
        if cls.__cur:
            # 关闭游标对象
            cls.__cur.close()

    # 私有类方法，封装关闭连接对象的方法
    @classmethod
    def __closeConn(cls):
        if cls.__conn:
            # 关闭连接对象
            cls.__conn.close()
