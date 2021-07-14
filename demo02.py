# a = 2
# b = 5
# if a > b:
#     print('a比b大')
# else:
#     print('b更大')




# a = '你好吗，我想你了'
# for i in a:
#     print(i)

# print(a[1:3])

# b = list(range(0,100,2))
# print(b)


# sum= 0
# i = 0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

# username = input('请输入你的账号：')
# password = input('请输入你的密码：')

# if len(username) >= 5 and len(username)<=8:
#     if username[0] in 'qwertyuiopasdfghjklzxcvbnm':
#         if len(password)>=6 and len(password)<=12:
#             print('打印成功',{username:password})
#         else:
#             print('密码必须6-12位')
#     else:
#         print('首字母必须是小写开头')
# else:
#     print('账号必须5-8位')


# i = 1 
# sum = 0
# while i<=99:
#     sum= sum + 1/i
#     i=i+2
# print(sum)



# def checkname(username):
#     '''
#     自动判断账号长度是5-8位，bing'qie 账号必须小写开头
#     '''
#     if len(username) >= 5 and len(username)<=8:
#         if username[0] in 'qwertyuiopasdfghjklzxcvbnm':
#             print('ok')
#         else:
#             print('首字母必须是小写开头')
#     else:
#         print('账号必须5-8位')
# # def  方法的声明
# checkname  方法的名字
# username 方法的参数
# 所有代码:方法的逻辑代码

# def jiafa(a,b):
#     '两个数字相加'
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         print('输入的数据类型错误')
    
# '''
# 返回值,返回后我们可以对这个值做其他操作,而print不能
# '''
# jiafa(5,9)


try:
    print('hhh'+15)
except Exception as e:
    print('上面的代码写错了',e)


    # 包->类->方法->变量

print('5'+'jjj')