#模拟管理员登录
from dbtools import chaxun
from dbtools import commit


# username = input ('请输入账号：')
# password = input ('请输入密码：')


# sql = "select * from t_admin WHERE username = '{}' and password = '{}';".format(username,password)
# print(sql)
# chaxun(sql)
# res = chaxun(sql)

# # 有结果
# if len(res) != 0:
#     print('管理员登陆成功！')
# else:
#     print('管理员登陆失败')


#------------- 注册的例子
username = input ('请输入账号：')
password = input ('请输入密码：')


sql = 