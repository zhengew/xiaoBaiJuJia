# # 在单继承中，super 就是找父类

class A:
    Hoby = 'running'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print('in A')

class B(A):
    def __init__(self, name, age, sex):
        super().__init__(name, age) # 在py3中这么用
        # super(B, self).__init__(name, age) # 在py2中这么用
        self.sex = sex
    def func(self):
        super(B, self).func()

# xb = B('xb', 10, 'M')
# print(xb.__dict__)
# xb.func()

# 在多继承中，super 遵循 mro方法
# 在py2中的经典类，没有mro方法，也就不支持super关键字

class A:
    def func(self):
        print('in A')
class B(A):
    def func(self):
        super().func()
        print('in B')
class C(A):
    def func(self):
        super().func()
        print('in C')

class D(B, C):
    def func(self):
        super().func()
        print('in D')

D().func()
# 这种多继承 首先 广度优先，遵循mro方法, 乌龟模型的 顺序 D, B, C, A,
# 所有实例化D() 在调用func()时， 先执行 super().func() ,会优先按照 mro原则找父类， 最后找到的是A中的 func 打印 in A， 之后是C 打印 in C， 在之后 B 打印 in B, 最后是 D 打印 in D
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]




# class A:
#     def func(self):
#         print('in A')
# class B(A):
#     def func(self):
#         print('in B')
# class C(A):
#     def func(self):
#         print('in C')
#
# class D(B, A):
#     def func(self):
#         print('in D')
#
# D().func() # in D  子类中有所以打印 in D

