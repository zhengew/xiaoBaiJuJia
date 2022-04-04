'''
# 反射：用字符串数据类型的名字来操作这个名字对应的函数\实例变量\绑定方法\各种方法
'''

# name = 'alex'
# age = 123
#
# n = input('>>>')
# if n == name:print(name)
# elif n == age:print(age)

# 有些时候，你明明知道一个变量的字符串数据类型的名字，你想直接调用它，但是调不到, 使用反射.
''' 反射的使用场景 '''
''' 1. 反射对象的实例变量 '''
''' 2. 反射类的 静态变量/绑定方法/其他方法 '''
''' 3. 模块中的所有变量
        # 被导入的模块      
        # 当前模块的py文件  - 脚本
'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def qqxing(self):
#         print('qqxing')
#
# alex = Person('alex', 83)
# wusir = Person('wusir', 74)
#
# ret = getattr(alex,'name')
# print(ret)
# ret = getattr(wusir,'name')
# print(ret)
# ret = getattr(wusir,'qqxing')
# ret()

# class Payment:pass
#
# class Alipay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'uname':self.name, 'price':money}
#         # 想办法调用支付宝支付 url连接 把dic传过去
#         print('%s通过支付宝支付%s钱成功' %(self.name, money))
#
# class WeChat(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username':self.name, 'monye':money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功' %(self.name, money))
#
# class Apple(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username': self.name, 'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))
#
# aw = WeChat('alex')
# aw.pay(400)
# aa = Alipay('alex')
# aa.pay(400)
#
# # 归一化设计
# def pay(name, price, kind):
#     if kind == 'Wechat':
#         obj = WeChat(name)
#     elif kind == 'Alipay':
#         obj = Alipay(name)
#     elif kind == 'Apple':
#         obj = Apple(name)
#
#     obj.pay(price)
#
# pay('alex', 400, 'Wechat')
# pay('alex', 400, 'Alipay')
# pay('alex', 100, 'Apple')

# import a
# print(a.Wechat)
# print(a.Alipay)
# 对象名.属性名 ==> getattr(对姓名, '属性名')
# a.Alipay == > getattr(a, 'Alipay')
# print(getattr(a, 'Alipay')) # <class 'a.Alipay'>
# print(getattr(a, 'Wechat')) # <class 'a.Wechat'>
# 'Wechat'
# 'Alipay'


# import a
# import sys
# print(sys.modules['a'].Alipay)
# print(a.Alipay)
# print(getattr(a, 'Alipay'))
# print(getattr(sys.modules['a'], 'Alipay'))
#
# wahaha = 'hahaha'
# print(getattr(sys.modules['__main__'], 'wahaha'))


''' 利用反射优化 归一化设计 '''

# class Payment:pass
#
# class Alipay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'uname':self.name, 'price':money}
#         # 想办法调用支付宝支付 url连接 把dic传过去
#         print('%s通过支付宝支付%s钱成功' %(self.name, money))
#
# class WeChat(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username':self.name, 'monye':money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功' %(self.name, money))
#
# class Apple(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username': self.name, 'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))
#
# class QQpay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'username': self.name, 'number': money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过QQ支付%s钱成功' % (self.name, money))
#
# import sys
# aw = WeChat('alex')
# aw.pay(400)
# aa = Alipay('alex')
# aa.pay(400)

'''归一化设计 '''
# def pay(name, price, kind):
#     # 反射优化版本
#     class_name = getattr(sys.modules['__main__'], kind)  # 通过反射获取了本文件中对应类的内存地址
#     obj = class_name(name)
#     obj.pay(price)

    # 原始版本
    # if kind == 'Wechat':
    #     obj = WeChat(name)
    # elif kind == 'Alipay':
    #     obj = Alipay(name)
    # elif kind == 'Apple':
    #     obj = Apple(name)
    #
    # obj.pay(price)

# pay('alex', 400, 'WeChat')
# pay('alex', 400, 'Alipay')
# pay('alex', 100, 'Apple')
# pay('alex', 100, 'QQpay')

''' 反射的使用场景 '''
''' 1. 反射对象的实例变量 '''
''' 2. 反射类的 静态变量/绑定方法/其他方法 '''
''' 3. 模块中的所有变量
        # 被导入的模块      
        # 当前模块的py文件  - 脚本
'''

# class A:
#     Role = '法师'
#     def __init__(self):
#         self.name = 'alex'
#         self.age = 84
#     def func(self):
#         print('wahaha')
#         return 666
# a = A()
# print(getattr(a, 'name')) # 反射对象的实例变量
# print(getattr(a, 'func')()) # 反射对象的绑定方法
# print(getattr(A, 'Role'))  # 反射类中的静态变量
#
# import a # 引用模块中的任意的变量
# print(getattr(a, 'sww'), a.sww)
# getattr(a, 'sww')()
# print(getattr(a, 'lst'), a.lst)
# print(getattr(a, 'dic'), a.dic)
# print(getattr(a, 'we'), a.we)

import sys # 反射本模块中的内容
cat = '小a'
dog = '小b'
def pig():
    print('小p')
print(getattr(sys.modules['__main__'], 'cat'))
print(getattr(sys.modules['__main__'], 'dog'))
getattr(sys.modules['__main__'], 'pig')()

