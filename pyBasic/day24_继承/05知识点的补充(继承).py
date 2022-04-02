'''
# object 类 类祖宗
# 所有在pyton3当中的类，都继承自object类

一：我们定义的类的属性到底存到哪里了？有两种方式查看
dir(类名)：查出的是一个名字列表
类名.__dict__:查出的是一个字典，key为属性名，value为属性值

二：特殊的类属性
类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串
类名.__base__# 类的第一个父类(在讲继承时会讲)
类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)

'''

# object 中有 init
# 所有的类都默认的继承object

# class A:pass
# a = A()
# 开辟内存空间
# 调用 init

'''__bases__ 查看类的父类(只显示父类) '''
# class A:pass
# class B(A):pass
# print(A.__bases__) # (<class 'object'>,)
#
# class C:pass
# class B(A, C):pass
# print(B.__bases__) # (<class '__main__.A'>, <class '__main__.C'>)

''' 
绑定方法和普通的函数
'''
from types import FunctionType, MethodType
# FunctionType 函数
# MethodType 方法

# instance type  判断类型以及判断类与类的继承关系
# a = 1
# b = 'abc'
# print(isinstance(a, int))
# print(isinstance(a, float))
#
# print(type(a) is int)
# print(type(b) is str)
#
# class Cat:pass
#
# xb = Cat()
#
# print(type(xb) is Cat)
# print(isinstance(xb, Cat))
#
# class A:
#     def func(self):
#         print('in func')
#
# print(A.func) # 函数 # <function A.func at 0x106b61550>
# a = A()
# print(a.func) # 方法 # <bound method A.func of <__main__.A object at 0x106c2df70>>
#
# print(isinstance(a.func, FunctionType)) # False
# print(isinstance(a.func, MethodType)) # True
# print(isinstance(A.func, FunctionType)) # True
# print(isinstance(A.func, MethodType)) # False
# print(a.__class__) # <class '__main__.A'>




