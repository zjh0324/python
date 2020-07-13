import pymysql


def chaxun(sql):
    '''
    查询MySQL数据库,不要delete,update,insert
    '''
    # 用pymysql 连接数据库
    db = pymysql.connect(host = '192.144.148.91',user = 'ljtest',password = '123456',db='ljtestdb')
    # 获取游标  :查询窗口
    cur = db.cursor() 
    # 执行SQL语句
    cur.execute(sql) 
    #  得到执行的结果
    res = cur.fetchall()
    db.close()

    return res 

# sql = 'select * from t_user where id = 255;'
# a = chaxun(sql)
# print(a)



def commit(sql):
    '''
    增加/删除/修改方法：delete update insert ,不要传select
    '''
    # 用pymysql 连接数据库
    db = pymysql.connect(host = '192.144.148.91',user = 'ljtest',password = '123456',db='ljtestdb')
    # 获取游标  :查询窗口
    cur = db.cursor() 
    # 执行SQL语句
    cur.execute(sql) 
    #  提交修改
    db.commit()
    db.close()

    return True

# sql = "update t_user set username ='mcc123' where id = 254;"

# commit(sql)