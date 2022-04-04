''' 注解 property

'''
# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property   # 把一个方法伪装成一个属性，在调用这个方法的时候不需要加() 就可以直接得到方法的返回值
#     def area(self):
#         return pi * self.r ** 2
#
# c1 = Circle(5)
# print(c1.r)
# print(c1.area)

# 变量的属性和方法？
    # 属性：圆形的半径/圆形的面积
    # 方法：登陆 注册

''' property 装饰的这个方法，不能有参数 '''
# import time
# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = 1998
#     @property
#     def age(self): # property 装饰的这个方法，不能有参数
#         return time.localtime().tm_year - self.birth
#
# tb = Person('太白', 1998)
# print(tb.age)

''' property 的第二个应用场景: 和私有的属性合作的 '''
# class User:
#     def __init__(self, usr, pwd):
#         self.usr = usr
#         self.__pwd = pwd
#
#     @property
#     def pwd(self):
#         return self.__pwd
#
# alex = User('alex', 'sbsbsb')
# print(alex.pwd)
# alex.pwd = 123456 # AttributeError: can't set attribute

''' property 的第三个应用场景：和类的静态变量合作 '''
# class Goods:
#     discount = 0.8 # 静态变量
#     def __init__(self, name, origin_price):
#         self.name = name
#         self.__price = origin_price
#
#     @property
#     def price(self):
#         return self.__price * self.discount
#
# apple = Goods('apple', 5)
# print(apple.price)

''' property 进阶 '''
# class Goods:
#     discount = 0.8 # 静态变量
#     def __init__(self, name, origin_price):
#         self.name = name
#         self.__price = origin_price
#
#     @property
#     def price(self):
#         return self.__price * self.discount
#     @price.setter
#     def price(self, new_value):
#         if isinstance(new_value, int):
#             self.__price = new_value
#
# apple = Goods('apple', 5)
# print(apple.price)  # 调用的是被 @property 装饰的 price
# apple.price = 10.0    # 调用的是被 @setter 装饰的 price
# print(apple.price)


''' 删除 '''
class Goods:
    discount = 0.8 # 静态变量
    def __init__(self, name, origin_price):
        self.name = name
        self.__price = origin_price

    @property
    def price(self):
        return self.__price * self.discount

    @price.setter
    def price(self, new_value):
        if isinstance(new_value, int):
            self.__price = new_value

    @price.deleter
    def price(self):
        # print('执行我了')
        del self.__price

apple = Goods('apple', 5)
print(apple.price)
apple.price == 'abcvd'
del apple.price  # 并不能真的删除什么，只是调用对应的被 @price.deleter装饰的方法而已
print(apple.price) # AttributeError: 'Goods' object has no attribute '_Goods__price'