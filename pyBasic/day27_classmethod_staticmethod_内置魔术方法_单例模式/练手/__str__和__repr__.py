'''
__str__
__repr
'''

# class Course:
#     def __init__(self, cname, price, period):
#         self.cname = cname
#         self.price = price
#         self.period = period
#
#     # def __str__(self):
#     #     return ','.join([self.cname, str(self.price), self.period])
#
# py22 = Course('python', 21800, '6 months')
# linux = Course('linux', 19800, '4 months')
#
# # 如果没有实现 __str__ 打印的是 对象内存地址
# print(py22)  # <__main__.Course object at 0x107b1cfd0>

# class Course:
#     def __init__(self, cname, price, period):
#         self.cname = cname
#         self.price = price
#         self.period = period
#
#     def __str__(self):
#         return ','.join([self.cname, str(self.price), self.period])
#
# py22 = Course('python', 21800, '6 months')
# linux = Course('linux', 19800, '4 months')
# lst = [py22, linux]
# for index, opt in enumerate(lst, 1):
#     print(index, opt)
# # 1 python,21800,6 months
# # 2 linux,19800,4 months
#
# # %s 字符串拼接
# print('我们py22班 %s' % py22) # 我们py22班 python,21800,6 months
# # str() 方法
# print(str(py22)) # python,21800,6 months

class clas:
    def __init__(self):
        self.student = []
    def append(self, name):
        self.student.append(name)
    def __str__(self):
        return str(self.student) # __str__ 只能返回str类型，要注意数据类型转换问题


py22 = clas()

print(py22) # []
py22.append('大壮')
print('我们py22班 %s' % py22) # 我们py22班 ['大壮']
print(str(py22)) # ['大壮']
print(py22) # ['大壮']

# 在打印一个对象的时候，调用__str__方法
# 在 %s拼接一个对象的时候，调用__str__方法
# 在str(对象)的时候，调用__str__方法