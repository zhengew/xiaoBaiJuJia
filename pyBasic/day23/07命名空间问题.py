''' 类的成员和空间
'''

class A:
    Country = '中国' # 静态变量/静态属性  存储在类的命名空间里的
    def __init__(self): # 绑定方法 存储在类的命名空间里的
        pass
    def func1(self):
        print(self)
    def func2(self):pass
    Country = '印度'

a = A()
print(A.Country)
print(A.func1(1))
# print(A.__dict__)

a.func1() # == A.func1(a)