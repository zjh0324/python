'''
print('hello world')
print(True)
print(2)
print(3.8)
print((2,'金坷垃'))
print([False,8,'据了解哦i'])
print({'key':'values','name':'张三'})
print('jljio',53,None)
print('我今年'+'23岁了'+'你呢')
print('i like you'*10)
print((3*20*10-82)/10)
print(3>8)
print(8*2<10)
'''
# input获取的都是字符串
# a=input('请输入：')
# b=input('请输入：')
# print(a+b)
# 数据格式的转换
# print(type(1))
# print(type(2.5))
# print(type('lkj'))
# print(type(False))
# print(type(()))
# print(type([]))
# print(type({}))
# a='lj'
# b=256 
# d={'jl':3}
# c='256{}{}{}'.format(a,b,d)
# print(c)
# print(a.find('l'))
# a1=a.replace('lj','hhhhhh')
# print(a1)
# a=None
# print(type(a))
# a=[1,5,35,24,5,3,18,64,45]
# a.sort() #排序，从小到大
# print(a)
# a.sort(reverse=True)#从大到小排序
# print(a)
a='(3,4,5)'
a1=eval(a)
print(type(a1),a1)