#元组    tuple  不可变
# a = ('hh',5,'好好学习，天天向上',True,(1.3,5),False,{'jian':2})
# print(type(a[6]))
# print(a[4][0])
# print(a[-2:-1])
# print(len(a))
"""
# 数组  list  可变的
a=[2.5,8,'好好',True,None,(2,'hh')]
b=[2,5,8,3,5,9]
a.append('m')           #添加
print(a)
a.insert(1,False)       #添加
print(a)
a.remove(1)             #删除
print(a)
a[2]='Python简直太好玩了'  #修改
print(a)
b.sort()        #排序
print(b)
"""
#字典 dictionary
a={'name':'张三','age':22,'sex':'男','high':180}
#取值
v=a['name']
v1=a.get('sex')
v2=a.get('hh')
print(v,v1,v2)
#修改
a['name']='李四'
print(a)
#删除
del a['name']
print(a)
#添加
a['name']='Ekko'
print(a)