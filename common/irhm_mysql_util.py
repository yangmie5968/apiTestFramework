# 1.导包 pymysql
import pymysql


# 创建一个 类对象
class DBUtil(object):
    # 定义一个 连接 的全局变量
    conn = None

    # 封装数据库创建 conn 连接方法 ,因为调用方不关心，所以设置为私有方法，
    @classmethod  # 类方法上一行添加装饰器
    def __connect_db(cls):
        cls.conn = pymysql.connect(
            host="211.103.136.244",
            port=7061,
            user="student",
            password="iHRM_student_2021",
            database="ihrm",
            charset="utf8")
        # return conn(返回连接) 为了查询或者增删改方法 获取连接 conn 对象
        return cls.conn

    # 封装数据库关闭close，定义成私有方法
    @classmethod
    def __close_db(cls):
        cls.conn.close()

    # 对 sql语句 数据的封装 (语法和增删改的不同)
    @classmethod  # 类方法上一行添加装饰器
    def get_one(cls, sql):
        # 定义游标和查询返回结果的局部变量
        # 不定义也没有关系，为的是消除pycharm 代码规范的问题
        cursor = None
        resp = None
        try:
            # 创建连接conn，此时的conn 必须是创建好的连接conn，
            # 如果是None的话，没有办法获取游标cursor
            cls.conn = cls.__connect_db()
            # 获得游标cursor
            cursor = cls.conn.cursor()
            # 执行查询语句,获取结果，并且返回结果
            cursor.execute(sql)
            # 设置游标位置游标位置 = 0
            # cursor.rownumber = 0
            # 从结果集中，提取一行
            result = cursor.fetchone()
            print('查询数据库一行数据:', result)
        except Exception as err:
            print('数据库错误描述:', str(err))
        finally:
            # 关闭游标cursor
            cursor.close()
            # 关闭连接conn
            cls.__connect_db()
            # 最后返回查询结果,如果放在前面的话，后面的代码就不执行了
            return resp

    # 对数据 增删改 的封装
    @classmethod
    def uid_db(cls, sql):
        # 定义游标和查询返回结果的局部变量
        cursor = None
        try:
            # 创建连接 conn(如果不调用__connect_db(), conn的值为全局变量的值 None)
            cls.conn = cls.__connect_db()
            # 获得游标cursor
            cursor = cls.conn.cursor()
            # 执行 增删改 SQL语句 获取结果，并且返回结果
            cursor.execute(sql)
            #  查看修改数据库的行数 conn.affected_rows()
            affect_rows = cls.conn.affected_rows()
            print('查看修改数据库的行数:', affect_rows)
            # 事务提交
            cls.conn.commit()
        except Exception as err:
            print('增删改数据库错误问题描述:', str(err))
            #  事务回滚
            cls.conn.rollback()
        finally:
            # 关闭游标cursor
            cursor.close()
            # 关闭连接conn
            cls.__close_db()



if __name__ == '__main__':
    # 调用查询语法
    DBUtil.get_one("SELECT * FROM bs_user where id = 1539058451525697536;")
    # 调用增加语法
    # DBUtil.uid_db(" insert into bs_user (username,mobile,workNumber) values( 老6,17612535894,'123456);")
    # 调用修改语法
    # DBUtil.uid_db("update 表名 set `read` = `read` +250 where id = 5;")
    # 调用删除语法
    # DBUtil.uid_db("DELETE  from bs_user where `id` = 1539058451525697536;")
