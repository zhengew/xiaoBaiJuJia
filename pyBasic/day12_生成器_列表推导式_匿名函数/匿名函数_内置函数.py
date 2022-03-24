''' 匿名函数 lambda
语法: 函数名 = lambda 形参:返回值
func = lambda a, b : a + b
'''
# 练习1：接收一个可切片的数据，返回索引为0与2的对应的元素
# info = "abcdefg"
# func = lambda x : (x[0], x[1])
# print(func(info))

# 练习2：接收两个int参数，将较大的数据返回
# maxNum = lambda a, b : a if a > b else b
# print(maxNum(1, 2))

''' 内置函数 '''
# 1. 面向对象之前 重点讲解
# 1> abs 绝对值
# print(abs(-1)) # 1

# 2> enumerate 枚举值, 默认从0开始，可指定初始序号值，元组形式
# lis = ['a', 'b', 'c']
# for i in enumerate(lis, 1):
#     print(i)
'''
(1, 'a')
(2, 'b')
(3, 'c')
'''

# filter 过滤
'''
# 语法： filter(function,iterable)
# function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,然后根据function返回的True或者False来判断是否保留此项数据
'''
# lis = [i for i in range(30)]
# func = filter(lambda num : num % 3 == 0, lis) # 结合匿名函数，过滤不能被3整除的数字
# print(func, type(func)) # <filter object at 0x1100759a0> <class 'filter'>
# print(list(func)) # 需要将filter的返回值转换成list 或者 for循环遍历
# for i in func:
#     print(i, end=" ")


# map 映射
'''
语法：map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别去执行function
'''
# 计算列表中每个元素的平方，返回新列表
lis1 = [1, 2, 3, 4]
lis2 = map(lambda i : i*i, [1, 2, 3])
print(lis2, type(lis2)) # <map object at 0x10d852b50> <class 'map'>
print(list(lis2)) # [1, 4, 9]

# 总结：filter 是通过function的执行结果过滤数据，map则用可迭代对象中的每个元素去执行函数

# max 最大值
# min 最小值
# open 打开文件, os 级别的操作
# range 迭代数据 range(10) - > 0~8, 可指定初始值以及步长
# print 打印
# len 可迭代对象的长度
# list 列表
# dict 字典
# str 字符串
# float 浮点数

# reversed 将可迭代对象翻转,返回翻转后的迭代器
# lis = [1, 2, 3]
# lis2 = reversed(lis)
# print(lis2) # <list_reverseiterator object at 0x10e2d4a30>
# print(list(lis2)) # [3, 2, 1]

# set 集合

# sorted 排序
# lis = [1, 2, 3, 5, 4]
# lis = sorted(lis)
# print(lis)

# sum 求和
# tuple 元组
# type 数据类型

# zip 将可迭代对象作为参数，将对象中对应的元素作为一个个元组，然后返回元组；如果可迭代对象的元素数量不一样,按长度最短的返回
# a = "abc"
# b = "bcd"
# c = "abcdefg"
# for i in zip(a, b, c):
#     print(i)
''' 返回结果按找可迭代对象的索引位置依次返回
('a', 'b', 'a')
('b', 'c', 'b')
('c', 'd', 'c')
'''

# dir 字典

''' 面向对象是讲解 '''
# classmethod
# delattr
# getattr
# hasattr
# issubclass
# isinstance
# object
# property
# setattr
# staticmethod
# super