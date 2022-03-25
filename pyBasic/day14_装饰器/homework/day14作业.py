# 2. 读取register.txt 文件，模拟登陆博客园

# 3.看代码写结果：
#
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
#
# def func():
#     print(333)
#
# print(444)
# func()
# print(555)
'''444'''
'''333'''
'''555'''



# 4.编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret = func(*args, **kwargs)
#         return ret
#     return inner
#
# @wrapper
# def B_B():
#     print('123456')
#
# B_B()

# 5.为函数写一个装饰器，把函数的返回值 +100 然后再返回。
#
# @wrapper
# def func():
#     return 7
#
# result = func()
# print(result)
# def wrapper(func):
#     def inner(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         return ret + 100
#     return inner
# @wrapper
# def func():
#     return 7
#
# result = func()
# print(result)


# 6.请实现一个装饰器，通过一次调用是函数重复执行5次。
# def wrapper(func):
#     lst = []
#     def inner(*args, **kwargs):
#         i = 5
#         while i:
#             lst.append(func(*args, **kwargs))
#             i -= 1
#         return lst
#     return inner
# @wrapper
# def gogo():
#     print('111')
#
# gogo()

#
# 7.请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
#
# 可用代码：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
#
# def wrapper():
#     pass
# def func1(f):
#     print(f.__name__)
# func1(wrapper)
# 函数名通过： 函数名.__name__获取。


# def wrapper(func):
#     def inner(*args, **kwargs):
#         with open('student_msg.txt', mode='r+', encoding='utf-8') as f1:
#             import time
#             struct_time = time.localtime()
#             f1.seek(0,2)
#             f1.write(time.strftime("%Y-%m-%d %H:%M:%S", struct_time) + '\n')
#             print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))  # 当前时间节点
#             ret = func(*args, **kwargs)
#         return ret
#     return inner
# @wrapper
# def func1(f):
#     print(f.__name__)
#
# func1(wrapper)


