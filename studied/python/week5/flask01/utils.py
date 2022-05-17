import time
import pymysql
#获取系统时间函数
def get_time():
    time_str=time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")
#2.封装查询cov.sql数据库函数，导入数据库包，
#(1)定义封装一个链接
def get_cnn():
    """"
    :return:
    """
    #创建连接
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        db="cov",
        charset="utf8"
    )
    #封装游标
    cursor=conn.cursor() #执行完毕返回的结果集是默认以元组显示
    return conn,cursor

#(2)关闭链接和游标
def close_conn(conn,cursor):
    cursor.close()
    conn.close()

#（3）封装通用查询
def query(sql,*args):
    conn,cursor=get_cnn()
    cursor.execute(sql,args)
    res=cursor.fetchall()
    close_conn(conn,cursor)
    return res
#测试查询
def test():
    #定义查询语句
    sql="select * from details"
    #调用通用封装查询
    res=query(sql)
    return res[0]


#编写c1中间四个数字查询
def get_c1_data():
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)
    return res[0]



#测试
if __name__ == '__main__':
    print(get_c1_data())
    #print(test())

