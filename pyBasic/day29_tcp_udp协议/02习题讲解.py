class Foo(object):
    def __init__(self, num):
        self.num = num

# v1 = [Foo for i in range(10)]      # 10个类的地址
# v2 = [Foo(5) for i in range(10)]   # 10个不同的对象的地址  每个实例化对象有自己的内存空间
# v3 = [Foo(i) for i in range(10)]   # 10个不同的对象的地址
#
# print(v1)
# print(v2)
# print(v3)

# obj1 = Foo(10)
# print(obj1)
# obj2 = Foo(10)
# print(obj2)
# <__main__.Foo object at 0x10edc6fd0>
# <__main__.Foo object at 0x10edc6ee0>

# print(Foo(10))
# print(Foo(10))
# <__main__.Foo object at 0x10edc6e20>
# <__main__.Foo object at 0x10edc6e20>

# 值 是否被引用？
# print(1)
# a = 1
# 如果创建的对象没有被引用，那仅仅是在内存中开辟了一块空间，迟早会被gc回收掉


# Person1  Person2
# name = name
# age = age

class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):   # 两个对象作比较的时候会自动调用这个方法
        return self.name == other.name and self.age == other.age
    def __gt__(self, other): # __gt__ 大于
        print('执行gt啦')
    def __lt__(self, other): # __lt__ 小于
        print('执行lt啦')
alex = Person('alex',84)
alex222 = Person('alex',84)
print(alex == alex222)
    # == 符号刚好会调用alex对象对应的类的__eq__方法,alex222会被当做other参数传入方法
    # alex == alex222的结果就是__eq__方法的返回值

# # print(alex is alex222)
# alex<alex222
# alex>alex222