''' 函数名 '''
# 1. 函数名作为变量，实际指向的是函数在内存中的地址
# def func():
#    return 1
# print(func, type(func)) # <function func at 0x1029de1f0> <class 'function'>

# 2. 将函数名作为变量赋值给其他变量，那么被赋值的变量也就指向了原函数在内存中的地址，也就具有了原函数的功能
# def func():
#     print(2)
# a = func
# a() # 2

# 3.函数名可以当作容器类的元素
# def func():
#     return 1
#
# list = [1, 2, func]
# for i in list:
#     print(i)

# 4.函数名可以当作函数的参数
# def func1():
#     print("func1")
#
# def func2(func):
#     print("func2")
#     func()
#
# func2(func1)

# 5.函数名可以作为函数的返回值
# def func1():
#     print("in func1")
#
# def func2(func):
#     print("in func2")
#     return func
#
# a = func2(func1)
# a()


''' 格式化输出 py3.X新特性，有些时候也不适用的 '''
# 格式化输出的三种方式，各有各的用处，都需要掌握
# name = "zew"
# age = 31
# sex = "Man"
#
# infos = f"Name:{name}, Age:{age}, Sex:{sex}"
# print(infos)
#
# infos = "Name:%s, Age:%d, Sex:%s" % (name, age, sex)
# print(infos)
#
# infos = "Name:{}, Age:{}, Sex:{}".format(name, age, sex)
# print(infos)


''' 迭代器 '''

# 1.判断一个对象是不是可迭代对象: 凡事含有 __iter__方法的对象，都是可迭代对象
# dir() 会以列表形式返回对象的所有方法

# 示例: 判断对象是否为可迭代对象:
# infos = "abcd"
# print(dir(infos))

# def isIterObj(obj):
#     if "__iter__" in dir(obj):
#         return True
#     else:
#         return False
#
# print(isIterObj(infos))

# 2. 判断一个对象是否是迭代器: 内部含有 __iter__ 和 __next__方法的对象就是迭代器，例如 文件句柄
# def isIterNext(obj):
#     if "__iter__" in dir(obj) and "__next__" in dir(obj):
#         return True
#     else:
#         return False
#
# info = "abc"
# f = open(file=".//test.txt", mode="w", encoding="utf-8")
#
# print(isIterNext(info))
# print(isIterNext(f))

# 3.将可迭代对象转化为迭代器: obj.__iter__() or iter(obj)
# info = "abc"
# print(isIterNext(info))
#
# info = info.__iter__()
# print(isIterNext(info))
#
# lis = [1, 2, 3]
# lis = iter(lis)
# print(isIterNext(lis))


# 3.迭代器如何取值？ 通过 __next__()方法取值，如果迭代器里的元素取完了，继续__next__()，会抛出 StopIteration异常

# lis = [1, 2, 3].__iter__()
# print(lis.__next__())
# print(lis.__next__())
# print(lis.__next__())
# print(lis.__next__()) # StopIteration

# 4.利用 while 模拟 for循环的内部机制

# lis = [1, 3, 4, 5]
# obj = iter(lis)
# 通过 next() 迭代的取出元素，如果抛出StopIteration异常，就break 终止循环
# while 1:
#     try:
#         print(next(obj))
#     except StopIteration:
#         break

''' 可迭代对象和迭代器的优缺点：
可迭代对象：
    是一个私有的方法比较多，操作灵活（比如列表，字典的增删改查，字符串的常用操作方法等）,比较直观，但是占用内存，而且不能直接通过循环迭代取值的这么一个数据集。
    应用：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。

迭代器：
    是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。
    应用：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。（可参考为什么python把文件句柄设置成迭代器）
'''

