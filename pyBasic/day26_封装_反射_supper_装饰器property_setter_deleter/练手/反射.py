''' 反射的使用场景 '''
import sys

''' 1. 反射对象的实例变量 '''
''' 2. 反射类的 静态变量/绑定方法/其他方法 '''
''' 3. 模块中的所有变量
        # 被导入的模块      
        # 当前模块的py文件  - 脚本
'''


#  1. 反射对象的实例变量,绑定方法
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         print(f'我叫{self.name},今年{self.age}岁.')
#
# xb = User('alex', 18)
# # 访问对象的实例变量
# print(getattr(xb, 'name')) # alex
# print(getattr(xb, 'age')) # 18
# # 访问对象的绑定方法
# print(xb.func, getattr(xb, 'func'))
# # <bound method User.func of <__main__.User object at 0x10b933fd0>> <bound method User.func of <__main__.User object at 0x10b933fd0>>
# getattr(xb, 'func')() # 我叫alex,今年18岁.


# 2. 反射类的 静态变量/绑定方法/其他方法

# class User:
#     Country = 'China' # 静态变量
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self): # 绑定方法
#         print(f"我叫{self.name}, 今年{self.age}岁, 国籍是:{self.Country}")
#
# print(getattr(User, 'Country')) # China  访问类中的静态变量
# print(getattr(User, 'func')) # <function User.func at 0x106d9f040>  访问类中的绑定方法的内存地址
# getattr(User('alex', 18), 'func')() # 我叫alex, 今年18岁, 国籍是:China 调用类中的绑定方法

# import a
# import sys
# print(getattr(a, 'User'), a.User) # 导入的a 模块中的 User类
# print(getattr(a, 'lis')) # 导入模块中的 静态变量
# print(getattr(a, 'alex')) # 导入模块中的实例对象
# print(getattr(a, 'alex').name) # 导入模块的实例对象的属性
# getattr(a, 'alex').func() # 导入模块的实例对象的绑定方法

# 反射当前模块中的
# print(sys.modules) # 当前模块或当前文件的 key是 '__main__'
# '__main__': <module '__main__' from '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day26_super 封装 反射/练手/反射.py'>,
class A:pass
a = 'abc'
b = [1, 2, 3]
def func():
    print(a, b)
print(sys.modules['__main__'])
print(getattr(sys.modules['__main__'], 'a')) # abc          本模块中的变量 a
print(getattr(sys.modules['__main__'], 'b')) # [1, 2, 3]    本模块中的变量 b
print(getattr(sys.modules['__main__'], 'func')) # <function func at 0x102d26550> 本模块 func的内存地址
getattr(sys.modules['__main__'], 'func')() # abc [1, 2, 3]  反射本模块中的方法 func的内存地址,并调用
print(getattr(sys.modules['__main__'], 'A')) # <class '__main__.A'>  反射的本模块中的A类