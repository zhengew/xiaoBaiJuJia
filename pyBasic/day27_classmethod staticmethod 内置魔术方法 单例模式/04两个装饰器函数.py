''' classmethod '''
class Goods:
    __discount = 0.8
    def __init__(self):
        self.price = 5
        self.price = self.price * self.__discount

    @classmethod # 把一个对象绑定的方法，修改成一个 类方法
    def change_discount(cls, new_discount):
        print(cls, Goods)
        cls.__discount = new_discount



''' @classmethod 被装饰的方法会成为一个类方法
# 把一个对象绑定的方法，修改成一个 类方法 '''
# 第一，在方法中仍然可以引用类中的静态变量
# 第二，可以不用实例化对象，就直接用类名在外部调用这个方法
# 什么时候用 @classmethod?
    # 1.定义了一个方法，默认传self，但这个self没被使用
    # 2. 并且你在这个方法里用到了当前的类名，或者你准备使用这个类的内存空间中的名字的时候
# Goods.change_discount(0.6)  # 类方法可以通过类名调用
# apple = Goods()
# print(apple.price)
#
# apple.change_discount(0.1) # 类方法可以通过对象名调用
# apple2 = Goods()
# print(apple2.price)

## 经典数据
# python 核心编程/基础教程/流畅的python/数据结构与算法(机械工业出版社)/cook book

''' 练习题 通过类中的方法直接拿到类的实例化对象，并操作实例化对象的属性 '''
# import time
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     @classmethod
#     def today(cls):
#         struct_t = time.localtime()
#         date = cls(struct_t.tm_year, struct_t.tm_mon, struct_t.tm_mday) # 在自己类里把自己实例化（先开空间在调init）
#         return date
# date = Date.today() # 这里实际拿到的是 Date类的实例化对象
# print(date.year)
# print(date.month)
# print(date.day)


''' @staticmethod 被装饰的方法会成为一个静态方法
'''

# class User:
#     pass
#
#     @staticmethod # 本身是一个普通的函数，被挪到类的内部执行，那么直接给这个函数添加@staticmethod装饰器就可以了
#     def login(a, b):
#         print('登陆逻辑', a, b)
#         # 在函数内部既不会用到self变量，也不会用到cls类
# obj = User()
# User.login(1, 2)
# obj.login(3, 4)

# class A:
#     county = 'China'
#     def func(self):
#         print(self.__dict__)
#     @classmethod
#     def clas_func(cls):
#         print(cls)
#     @staticmethod
#     def stat_func():
#         print('普通函数')
#     @property
#     def name(self):
#         return 'wahaha'

''' 能定义在类中的内容 '''
# 静态变量：是个所有对象共享的变量，由对象或类调用，但是不能重新赋值
# 绑定方法：是个自带self参数的函数，由对象调用
# 类方法：是个自带cls参数的函数，由对象或类调用
# 静态方法：是个啥都不带的普通函数，有对象或类调用
# property 属性：是个伪装成属性的方法，有对象调用，但不加括号