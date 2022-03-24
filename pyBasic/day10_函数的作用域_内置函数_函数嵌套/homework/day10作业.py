# # 1.写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
# def jia(a, b, c):
#     if type(a) == int and type(b) == int and type(c) == int:
#         return a+b+c
#
# #
# # 2.看代码写结果
# #
# #
# # def func():
# #     return 1, 2, 3
# #
# #
# # val = func()
# # print(type(val) == tuple)     True
# # print(type(val) == list)      False
#
#
#
#
# # 3.看代码写结果
# #
# #
# # def func(*args, **kwargs):
# #     pass
# #
# #
# # # a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# def func(*args, **kwargs):
#     return  args
#
# func(1, 2, 3, 4)
#
# # # b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# def func(*args, **kwargs):
#     return  args
#
# func([1, 2, 3, 4],[11, 22, 33])
#
#
# # # c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# def func(*args, **kwargs):
#     return  args,kwargs
#
# func([11, 22], 33, k1='v1', k2='v2')
#
# # # d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# #args:('武沛齐','金鑫','女神')
# #kwargs:{}
#
# # # e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
# #args:({'武沛齐','金鑫','女神'},[11,22,33])
# #kwargs:{}
#
# # # f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
# #args:('武沛齐','金鑫','女神',[11,22,33]})
# #kwargs:{'k1','栈'}
#
#
# # 4.看代码写结果
# #
# #
# # def func(name, age=19, email='123@qq.com'):
# #     pass
# #
# #
#
#
# # # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''可执行,name:'alex' age:19 email:'123@qq.com' '''
#
# # # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''可执行,name:'alex' age:20 email:'123@qq.com' '''
#
# # # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''不可执行 '''
#
# # # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''可执行,name:'alex' age:19 email:'x@qq.com' '''
#
# # # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''可执行,name:'alex' age:99 email:'x@qq.com' '''
#
# # # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''不可执行 '''
#
# # # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# '''不可执行 '''
# # 5.看代码写结果
# #
# #
# # def func(users, name):
# #     users.append(name)
# #
# #
# #     return users
# #
# # result = func(['武沛齐', '李杰'], 'alex')
# # print(result)
# '''['武沛齐', '李杰', 'alex' ]'''
#
#
#
#
#
#
# # 6.看代码写结果
# #
# #
# # def func(v1):
# #     return v1 * 2
# #
# #
# # def bar(arg):
# #     return "%s 是什么玩意？" % (arg,)
# #
# #
# # val = func('你')
# # data = bar(val)
# # print(data)
# '''你你 是什么玩意？'''
#
#
# # 7.看代码写结果
# #
# #
# # def func(v1):
# #     return v1 * 2
# #
# #
# # def bar(arg):
# #     msg = "%s 是什么玩意？" % (arg,)
# #     print(msg)
# #
# #
# # val = func('你')
# # data = bar(val)
# # print(data)
# '''你你 是什么玩意？'''
# '''None'''
#
# # 8.看代码写结果
# #
# # v1 = '武沛齐'
# #
# #
# # def func():
# #     print(v1)
# #
# #
# # func()
# # v1 = '老男人'
# # func()
# '''武沛齐'''
# '''老男人'''
#
# # 9.看代码写结果
# #
# # v1 = '武沛齐'
# #
# #
# # def func():
# #     v1 = '景女神'
# #
# #     def inner():
# #         print(v1)
# #
# #     v1 = '肖大侠'
# #     inner()
# #
# #
# # func()
# # v1 = '老男人'
# # func()
# '''肖大侠'''
# '''肖大侠'''
#
#
# # 10.看代码写结果【可选】
# #
# # def func():
# #     data = 2 * 2
# #     return data
# #
# #
# # new_name = func
# # val = new_name()
# # print(val)
# #
# # # 注意：函数类似于变量，func代指一块代码的内存地址。
# '''4'''
#
#
# # 11.看代码写结果【可选】
# #
# # def func():
# #     data = 2 * 2
# #     return data
# #
# #
# # data_list = [func, func, func]
# # for item in data_list:
# #     v = item()
# #     print(v)
# #
# # # 注意：函数类似于变量，func代指一块代码的内存地址。
# '''4'''
# '''4'''
# '''4'''
#
#
# # 12.看代码写结果（函数可以做参数进行传递）【可选】
# #
# # def func(arg):
# #     arg()
# #
# #
# # def show():
# #     print('show函数')
# #
# #
# # func(show)
# '''show函数'''
#
#
#
# # 13.写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def jiafa(*args):
#     s = 0
#     for j in args:
#         if type(j) != int:
#             return None
#     for i in args:
#         s += i
#     return s
#
#
#
#
# #
# # 14.读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# #
# # a = 10
# # b = 20
# #
# #
# # def test5(a, b):
# #     print(a, b)
# #
# #
# # c = test5(b, a)
# # print(c)
# '''a : 10 b : 20 '''
# '''c:None '''
#
#
#
#
# # 15.读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# # a = 10
# # b = 20
# #
# #
# # def test5(a, b):
# #     a = 3
# #     b = 5
# #     print(a, b)
# #
# #
# # c = test5(b, a)
# # print(c)
# '''a : 3 b : 5 '''
# '''c:None '''
#
#
# # 16.传入函数中多个列表和字典, 如何将每个列表的每个元素依次添加到函数的动态参数args里面？
# # 如何将每个字典的所有键值对依次添加到kwargs里面？
# '''列表:使用*lst'''
# '''字典:使用**dic'''
# '''例:'''
# def func(*args, **kwargs):
#     return  args,kwargs
#
# func(*[1, 2, 3, 4], **{'k1':'v1', 'k2':'v2'})
#
#
# # 17.写函数, 接收两个数字参数, 将较小的数字返回.
# #
# def func_deci(a, b):
#     if type(a) == int and type(b) == int:
#         return a if a < b else b
#
#
#
#
#
# # 18.写函数, 接收一个参数(此参数类型必须是可迭代对象), 将可迭代对象的每个元素以’_’相连接,
# # 形成新的字符串, 并返回.
# #
# # 例如
# # 传入的可迭代对象为[1, '老男孩', '武sir']
# # 返回的结果为’1
# # _老男孩_武sir’
# #
# from collections import Iterable
# def func_iter(seq):
#     if isinstance(seq, Iterable):
#         s = ''
#         for el in seq:
#             s += str(el) + '_'
#         s = s.strip('_')
#         return s
#
#
#
# # 19.
# # 有如下函数:
# #
# #
# # def wrapper():
# #     def inner():
# #         print(666)
# #
# #
# # wrapper()
# # 你可以任意添加代码, 执行inner函数.
# #
# def wrapper():
#     def inner():
#         print(666)
#
#     return inner()
#
# wrapper()
#
#
#
# # 相关面试题：
# # 20.写出下列代码结果：
# #
# # def foo(a, b, *args, c, sex=None, **kwargs):
# #     print(a, b)
# #
# #     print(c)
# #
# #     print(sex)
# #
# #     print(args)
# #
# #     print(kwargs)
#
# #
# # \  # foo(1,2,3,4,c=6)
#
# '''print(a, b):1 2'''
# '''print(c):6'''
# '''print(sex):None'''
# '''print(args):(3,4)'''
# '''print(kwargs):{}'''
#
# #
# # \  # foo(1,2,sex='男',name='alex',hobby='old_woman')
# '''报错'''
#
# #
# # \  # foo(1,2,3,4,name='alex',sex='男')
# '''报错'''
#
#
# #
# # \  # foo(1,2,c=18)
# '''print(a, b):1 2'''
# '''print(c):18'''
# '''print(sex):None'''
# '''print(args):()'''
# '''print(kwargs):{}'''
#
# #
# # \  # foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')
# '''print(a, b):2 3'''
# '''print(c):13'''
# '''print(sex):None'''
# '''print(args):([1, 2, 3],)'''
# '''print(kwargs):{hobby:'喝茶'}'''
#
# #
# # \  # foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})
# '''print(a, b):1 2'''
# '''print(c):12'''
# '''print(sex):女'''
# '''print(args):([3, 4])'''
# '''print(kwargs):{'name':'太白'}'''