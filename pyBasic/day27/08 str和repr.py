'''
__str__
__repr__
'''

# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#     def __str__(self):
#         return ','.join([self.name, str(self.price), self.period])
# python = Course('python', 21800, '6 months')
# linux = Course('linux', 19800, '5 months')
# mysql = Course('mysql', 12800, '6 months')
# go = Course('go', 15800, '6 months')
#
# # print(go)
# lst = [python, linux, mysql, go]
# for index, course in enumerate(lst, 1):
#     print(index, course)
'''
1 python,21800,6 months
2 linux,19800,5 months
3 mysql,12800,6 months
4 go,15800,6 months
'''

# for index, c in enumerate(lst, 1):
#     print(index, c)
#
# num = int(input('>>>'))
# course = lst[num-1]
# print('恭喜你选择的课程为%s, 价格为%s元' % (course.name, course.price))

# 版本一
# class clas:
#     def __init__(self):
#         self.student = []
#     def append(self, name):
#         self.student.append(name)
#
# py22 = clas()
# print(py22) # <__main__.clas object at 0x106501fd0>
# py22.append('大壮')
# print(py22) # <__main__.clas object at 0x106501fd0>

# 版本二 实现 __str__
# class clas:
#     def __init__(self):
#         self.student = []
#     def append(self, name):
#         self.student.append(name)
#     def __str__(self):
#         return str(self.student) # __str__ 只能返回str类型，要注意数据类型转换问题
#
#
# py22 = clas()
#
# print(py22) # []
# py22.append('大壮')
# print('我们py22班 %s' % py22) # 我们py22班 ['大壮']
# print(str(py22)) # ['大壮']
# print(py22) # ['大壮']

# 在打印一个对象的时候，调用__str__方法
# 在 %s拼接一个对象的时候，调用__str__方法
# 在str(对象)的时候，调用__str__方法

#

class clas:
    def __init__(self):
        self.student = []
    def append(self, name):
        self.student.append(name)
    def __repr__(self):
        return str(self.student)
    def __str__(self):
        # return str(self.student) # __str__ 只能返回str类型，要注意数据类型转换问题
        return 'aaa'

py22 = clas()
py22.append('大壮')
print(py22) # aaa
print(str(py22)) # aaa
print('我们py22班 %s' % py22) # 我们py22班 aaa
print('我们py22班 %r' % py22) # 我们py22班 ['大壮']
print(repr(py22)) # ['大壮']

# 当我们打印一个对象 用%s进行字符串拼接 或者str(对象),总是调用这个对象的__str__方法，
# 如果找不到__str__方法，就调用__repr__方法
# __repr__不仅是__str__的替代品，还有自己的功能
# 用 %r 进行字符串拼接 或者用 repr(对象) 的时候，总是调用这个对象的 __repr__方法

