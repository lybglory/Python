#导包
import pymysql
#创建连接
conn = pymysql.connect(host="192.168.188.131", user="litemall", password="litemall123456", database="litemall", port=3306, charset='utf8')
#创建游标
cursor = conn.cursor()
#添加用户的SQL语句
addr_sql="INSERT INTO `litemall`.`litemall_address`(`id`, `name`, `user_id`, `province`, `city`, `county`, `address_detail`, `area_code`, `postal_code`, `tel`, `is_default`, `add_time`, `update_time`, `deleted`) VALUES ('{}', '{}', '{}', '北京市', '市辖区', '朝阳区', '奥北北区', '110105', '', '{}', 1, '2022-03-27 19:01:01', '2022-03-27 19:01:01', 0);"
#循环插入数据
user_start = 100000
for i in range(100000):
    # 地址id和用户id一样，方便jmeter脚本公用一个id
    addr_id = user_start + i
    user_id = user_start + i
    username = "test" + str(user_id)
    mobile = "18888" + str(user_id)

    print("插入第{}条数据ID为{}".format(i+1, user_id))
    sql = addr_sql.format(addr_id, username, user_id, mobile)
    cursor.execute(sql)

    conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()