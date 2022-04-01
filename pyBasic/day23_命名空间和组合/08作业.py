# 8点之前 统计作业完成度,难点
# 作业笔记
    # 写每一个题的用时
    # 遇到的问题
    # 解决思路


#第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么
# 请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致
# (1)
# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#     def func1(self):
#         print(self)
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country)
# print(b.Country)
# print(A.Country)
'''
日本
英国
英国
'''

# (2)
# class A:
#     Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#     def func1(self):
#         print(self)
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国')
# a.Country[0] = '日本' # 此处改的是A类的静态变量 Country
# print(a.Country)
# print(b.Country)
# print(A.Country)
'''
日本
日本
日本
'''

# (3)
# class A:
#     Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#         self.Country = country
#     def func1(self):
#         print(self)
#
# a = A('alex',83,'印度')
# b = A('wusir',74,'泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country)
# print(b.Country)
# print(A.Country)
'''
日本
泰国
英国
'''
# #(4) 这个题有点疑问啊 ？
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
# print(a.Country)
# print(a.Country())
'''
 函数 Country的内存地址
 函数 Country的内存地址
'''

# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求
# 外圆面积-内圆面积(圆周率X大半径的平方-圆周率X小半径的平方\圆周率X（大半径的平方-小半径的平方）)。
# 公式：S环=π（R²-r²）。公式：S环=π(R+r)(R-r)=π(R+r)d，d为圆环的宽度。
from math import pi

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r

class Ring:
    def __init__(self, outer_r, inner_r):
        outer_r, inner_r = (outer_r, inner_r) if outer_r > inner_r else (inner_r, outer_r)
        self.out_r = Circle(outer_r)
        self.in_c = Circle(inner_r)

    def area(self):
        return self.out_r.area() - self.in_c.area()

    def perimeter(self):
        return self.out_r.perimeter() + self.in_c.perimeter()

# c1 = Circle(5)
# c2 = Circle(10)

r1 = Ring(10, 8)
print(r1.perimeter())

# 1.传递的半径大小的顺序问题
# 2.为什么要用组合

# 程序里有两个需求：和圆形和环形相关，求环形相关的内容的时候用到了圆的公示




# 第三大题:继续完成计算器和优化工作