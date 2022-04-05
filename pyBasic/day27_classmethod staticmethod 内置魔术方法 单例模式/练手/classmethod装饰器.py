# class Goods:
#     __discount = 1.0
#     def __init__(self, good, price):
#         self.good = good
#         self.price = price * self.__discount
#
#     @classmethod # 把对象绑定的方法，改成类方法，
#     def change_discont(cls, newdiscount):
#         cls.__discount = newdiscount
# Goods.change_discont(0.8) # 通过类名调用类方法
# apple = Goods('apple', 15)
# print(apple.price) # 12.0
# apple.change_discont(0.6) # 通过对象名调用类方法
# apple2 = Goods('apple', 15)
# print(apple2.price) # 9.0

''' 练习题 通过类中的方法直接拿到类的实例化对象，并操作实例化对象的属性 '''
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod # 在类方法中实例化Date类，并返回实例化对象
    def today(cls):
        struct_time = time.localtime()
        date = cls(struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday)
        return date

today = Date.today() # 接收通过 Date调用的类方法today实例化的对象
print(today.year, today.month, today.day) # 2022 4 5