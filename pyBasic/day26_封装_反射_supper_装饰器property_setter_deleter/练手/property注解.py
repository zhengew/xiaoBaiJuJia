# 可以直接像属性一样访问函数中的方法

# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     @property
#     def area(self):  # 将绑定方法伪装成属性，直接访问
#         return pi * self.r ** 2
#
# c = Circle(5)
# print(c.area) #  78.53981633974483
# print(c.__dict__) # {'r': 5}


# 场景一
# 对外界简介提供处理过的属性
# 例如 年龄，一般通过生日去推算，不会直接存age属性
# import time
# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#
#     @property  # 被property装饰的方法，不能有参数
#     def age(self):
#         return time.localtime().tm_year - self.birth
#
# tb = Person('tbjx', 1990)
# print(tb.age) # 32

# 场景二
# 和私有属性合作
# 对外提供对私有属性的查询或符合规范的修改接口
# import hashlib
# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.__pwd = pwd
#
#     @property  # 对外提供经过加密的私有属性数据
#     def pwd(self):
#         return hashlib.md5(f'{self.__pwd}{self.__pwd}'.encode('utf-8')).hexdigest()
#
# xb = User('tbjx', '123456')
# print(xb.pwd) # ea48576f30be1669971699c09ad05c94
# print(xb.__dict__) # {'name': 'tbjx', '_User__pwd': '123456'}

# 场景三
# 和类的静态变量合作
# 通过静态变量，对外返回经过加工的数据

# class Goods:
#     Discount = 0.80 # 商品折扣率
#     def __init__(self, name, orignal_price):
#         self.name = name
#         self.__price = orignal_price
#
#     @property
#     def price(self):
#         return round(self.__price * self.Discount, 2)
#
# apple = Goods('apple', 14.5)
# print(apple.price) # 11.6

# @被property注解的函数名.setter
# 被setter装饰的方法可以接收参数，并修改私有属性
# class Goods:
#     Discount = 0.80
#     def __init__(self,name, orignal_price):
#         self.name = name
#         self.__price = orignal_price
#     @property
#     def price(self):
#         return round(self.Discount * self.__price, 2)
#     @price.setter
#     def price(self, newprice):
#         if isinstance(newprice, int) or isinstance(newprice, float):
#             self.__price = newprice
#
# apple = Goods('apple', 15.5)
# print(apple.price) # 12.4
# apple.price = 18
# print(apple.price) # 14.4
# print(apple.__dict__) # {'name': 'apple', '_Goods__price': 18}

# @被property注解的函数名.deleter
# 被 deleter装饰过后
# 外部可以使用 del 方法名，删除属性
# 此处并不是真的删除，只是调用了被 deleter装饰的方法而已

class Goods:
    Discount = 0.80
    def __init__(self, name, orignal_price):
        self.name = name
        self.__price = orignal_price

    @property
    def price(self):
        return round(self.Discount * self.__price, 2)
    @price.setter
    def price(self, newprice):
        if isinstance(newprice, int) or isinstance(newprice, float):
            self.__price = round(newprice, 2)
    @price.deleter # 执行被deleter装饰的方法，外界创建的对象会无法访问 被property装饰的属性
    def price(self):
        del self.__price

apple = Goods('apple', 15.5)
print(apple.price) # 12.4
del apple.price # 删除 apple.price, 并不能真的删除什么，只是调用对应的被 @price.deleter装饰的方法而已
# print(apple.price) # AttributeError: 'Goods' object has no attribute '_Goods__price'
print(apple.__dict__) # {'name': 'apple'}, apple对象的 price 属性被删除
