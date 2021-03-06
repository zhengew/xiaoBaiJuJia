# 1.请写出下列代码的执行结果：
# 例一：
# def func1():
#     print('in func1')
# def func2():
#     print('in func2')
# ret = func1
# ret() # in func1
# ret1 = func2
# ret1() # in func2
# ret2 = ret
# ret3 = ret2
# ret2() # in func1
# ret3() # in func1

#     例二：
# def func1():
#     print('in func1' )
# def func2():
#     print('in func2' )
# def func3(x, y):
#     x()
#     print('in func3' )
#     y()
# print(111)
# func3(func2, func1)
# print(222)
#
# 执行结果：
'''
111
in func2
in func3
in func1
222
'''


#     例三（选做题）：
# def func1():
#     print('in func1' )
# def func2(x):
#     print('in func2')
#     return x
# def func3(y):
#     print('in func3')
#     return y
# ret = func2(func1)
# ret()
# ret2 = func3(func2) # ret2 - > func2
# ret3 = ret2(func1)  # ret3 - > func1
# ret3()
# 执行结果：
'''
in func2
in func1
in func3
in func2
in func1
'''


# 2.看代码写结果：
#
# def func(arg):
#     return arg.replace('苍老师', '***')
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
# run()
# def func(arg):
#     return arg.replace('苍老师', '***')
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
# data = run()
# print(data)

'''
Alex的女朋友***和大家都是好朋友
Alex的女朋友***和大家都是好朋友
None
'''

# 3.看代码写结果：
#
# DATA_LIST = []
# def func(arg):
#     return DATA_LIST.insert(0, arg)
# data = func('绕不死你')
# print(data)
# print(DATA_LIST)

'''
None
['绕不死你']
'''


# 4.看代码写结果：
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)

'''
你好呀
你好妹呀
你好呀
你好妹呀
你好呀
你好妹呀
'''
# 5.看代码写结果：
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
# func_list = [func, func, func]
#
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)

'''
你好呀
你好妹呀
你好呀
你好妹呀
你好呀
你好妹呀
'''


# 6.看代码写结果：
#
# def func():
#     return '烧饼'
#
# def bar():
#     return '豆饼'
#
# def base(a1, a2):
#     return a1() + a2()
#
# result = base(func, bar)
# print(result)
'''
烧饼豆饼
'''

# 7.看代码写结果：
# for item in range(10):
#     print(item)
#
# print(item)
'''
0
1
2
3
4
5
6
7
8
9
9
'''

# 8.看代码写结果：
#
# def func():
#     for item in range(10):
#         pass
#     print(item)
#
#
# func()

'''
9
'''


# 9.看代码写结果：
# item = '老男孩'
#
# def func():
#     item = 'alex'
#
#     def inner():
#         print(item)
#
#     for item in range(10):
#         pass
#     inner()
#
# func()
# print(item)

'''
9  为什么是9？20220324  局部命名空间不能修改全局变量，for 变脸时,item = 9, 所以最后调用 inner() 打印的 9
老男孩
'''

# 10.看代码写结果：
# l1 = []
#
# def func(args):
#     l1.append(args)
#     return l1
#
# print(func(1))
# print(func(2))
# print(func(3))
#
'''
[1]
[1, 2]
[1, 2, 3]
'''


# 11.看代码写结果：
# name = '太白'
#
# def func():
#     global name
#     name = '男神'
#
# print(name)
# func()
# print(name)

'''
太白
男神
'''

# 12.看代码写结果：
# name = '太白'
# def func():
#     print(name) # 局部命名空间，可以引用全局变量，但不可修改全局变量，如果必须修改，需要先用global 声明
# func()

'''
太白
'''

# 13.看代码写结果：
# name = '太白'
# def func():
#     print(name)
#     name = 'alex' # 局部命名空间不可以直接修改全局变脸，如果要修改，需要先用 global 声明
#
# func() # UnboundLocalError: local variable 'name' referenced before assignment
#
'''
报错了， 需global声明 # global name
'''


# 14.看代码写结果：
# def func():
#     count = 1
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     print(count)
#     inner()
#     print(count)
#
# func()
'''
nonlocal 声明变量时，可以访问局部命名空间的上层变量
1
2
2
'''

# 15.看代码写结果：
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123, []) # 看不懂了....
# list3 = extendList('a')
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)



# 16.看代码写结果：
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# print('list1=%s' % extendList(10))
# print('list2=%s' % extendList(123, []))
# print('list3=%s' % extendList('a'))

'''
[10]
[123]
[10, 'a']
'''

# 17.用你的理解解释一下什么是可迭代对象，什么是迭代器。
'''可迭代对象:一个操作简单灵活,效率较高,但是消耗内存的数据集'''
'''迭代器:一个操作单一,有惰性机制,效率相对较低,但是占用内存很少的数据集'''
# 18.如何判断该对象是否是可迭代对象或者迭代器？
'''print('__Iter__' in dir(对象))'''
'''print('__Iter__' in dir(对象) and '__next()__' in dir(对象))'''
# 19.写代码：用while循环模拟for内部的循环机制（面试题）。
#
# lst = [1, 2, 3, 4, 5]
# obj = iter(lst)
# while 1:
#     try:
#         print(next(obj))
#     except StopIteration:
#         break

# 20.写函数，传入n个数，返回字典
# {‘max’:最大值,’min’:最小值}
# 例如: min_max(2, 5, 7, 8, 4)
# 返回: {‘max’:8,’min’:2}(此题用到max(), min()内置函数)

# def maxMinNum(*args):
#     return {"max":max(args), "min":min(args)}
#
# print(maxMinNum(1, 2, 3, 5, 4))


# 21.写函数，传入一个参数n，返回n的阶乘
# 例如: cal(7)
# 计算7654321
# def func(arg):
#     sum = 1
#     for i in range(1, arg+1):
#         sum *= i
#     return sum
# print(func(3))

# 22.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(选做题)
# 例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]
# def func():
#     lis = ["红心", "草花", "方片", "黑桃"]
#     lis_new = []
#
#     for i in range(1, 14):
#         if i == 1:
#             i = "A"
#         elif i == 11:
#             i = "J"
#         elif i == 12:
#             i = "Q"
#         elif i == 13:
#             i = "K"
#
#         for j in lis:
#             lis_new.append((j,i))
#     return lis_new
#
# print(func())


# 23.写代码完成99乘法表.(选做题，面试题)
# 1 * 1 = 1
#
# 2 * 1 = 2
# 2 * 2 = 4
#
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
#
# ......
#
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

def func():
    for i in range(1, 10):
        for j in range(1,i+1):
            print("%5d * %d = %-5d" % (j, i, j*i), end="")
        print()
func()