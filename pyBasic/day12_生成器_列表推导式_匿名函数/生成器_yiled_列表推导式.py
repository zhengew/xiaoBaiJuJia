''' 生成器 '''

# 生成器函数
# 1. yield 关键字
# 如果函数体中含有 yield 关键字，就是生成器函数，那么再执行函数的时候，就不再是函数的执行了，而是获取了这个生成器对象
# 需要用next()方法来执行生成器
# def func(*args):
#     yield sum(args)
#
# print(func(1,2)) # <generator object func at 0x1100f0820>
#
# lis = func(1, 2, 3, 4)
# print(next(lis))
# print(next(lis)) # StopIteration

# 注意:当程序执行完最后一个yield,再执行next() 会抛出 StopIteration异常

''' yield 与 return 的区别
1.return一般再函数中只设置一个,他的作用是终止函数,并且有返回值
2.yield 在生成器中可以设置多个，他并不会终止函数，next会获取对应yield生成的元素.
'''

# 示例: 吃包子
# def eat(num):
#     for i in range(1, num+1):
#         yield "包子" + str(i)
#
# num = eat(10) # 将生成器对象赋值给变量num
#
# for i in range(10):
#     print(next(num)) # 通过next获取对应的生成器元素

''' yield from 关键字'''
# 1.python3中，yield from 可以直接把可迭代对象中的每一个元素作为生成器的结果返回.
# 示例对比 yield 和 yield from

# 1> yield
# def func1():
#     lis = [1, 2, 3]
#     yield lis
#
# infos = func1()
# print(next(infos)) # next() 返回的是列表lis


# 2> yield from
# def func2():
#     lis = [1, 2, 3]
#     yield from lis
#
# infos = func2()
# while 1:
#     try:
#         print(next(infos)) # next() 返回的是列表lis中的元素
#     except StopIteration:
#         break


# 3> 函数中存在多个 yield from,会从上往下依次返回 可迭代对象中的每个元素，并不会交替返回元素的
# def func3():
#     lis1 = [1, 2, 3]
#     lis2 = [4, 5, 6]
#     yield from lis1
#     yield from lis2
#
# infos = func3()
#
# while 1:
#     try:
#         print(next(infos), end=" ") # 1 2 3 4 5 6
#     except StopIteration:
#         break


''' 推导式 '''
# 1. 列表推导式

# 1> 循环模式
# lis = [i for i in range(1, 11)]
# print(lis)
# 2> 筛选模式
# lis = [i for i in range(1, 11) if i % 2 == 0]
# print(lis)
'''
# 练习题:
# 1.将10以内所有整数的平方写入列表
# lis1 = [i*i for i in range(11)]
# print(lis1)

# 2.100以内所有的偶数写入列表
# lis2 = [i for i in range(100) if i % 2 == 0]
# print(lis2)

# 3.从python1期到python100期写入列表lst
# lis3 = [f"python{i}" for i in range(1, 101)]
# print(lis3)

# 4.三十以内可以被三整除的数
# lis4 = [i for i in range(3, 30, 3)]
# print(lis4)

# 5.过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# lis5 = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
# lis5 = [i.upper() for i in lis5 if len(i) >= 3]
# print(lis5)

# 6.找到嵌套列表中名字含有两个‘e’的所有名字
# lis6 = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# lis6 = [j for i in lis6 for j in i if j.count("e") == 2]
# print(lis6)
'''

''' 生成器表达式 
语法和列表推导式相同，只是把 [] 换成了 ()
'''
# 示例1.十以内所有数的平方放到一个生成器表达式中
# generate = (i*i for i in range(1, 10))
# print(generate) # <generator object <genexpr> at 0x10e967820>
#
# while 1:
#     try:
#         print(next(generate))
#     except StopIteration:
#         break

''' 生成器表达式和列表推导式的区别：
1.列表推导式 内存开销大，所有数据一次性写到内存中；生成器表达式遵循迭代器协议，逐个产生元素.
2.返回值不一样, 列表推导式返回的是列表；生成器表达式返回的是一个生成器
3.列表推导式一目了然，生成器表达式只是一个内存地址，需要用 next()依次获取生成器中的元素
'''

''' 字典推导式 
将两个列表分别当作字典的key 和 Value,实际的用处可能不大
'''
# lis1 = ["Name", "Age"]
# lis2 = ["ltt", "33"]
# infos = {lis1[i]:lis2[i] for i in range(len(lis1))} # {'Name': 'ltt', 'Age': '33'}
# print(infos)

''' 集合推导式
默认支持去重，用法和列表推导式相同，{}
'''
# lis1 = [1, 1 ,2 ,3]
# set1 = {i for i in lis1} # {1, 2, 3}
# print(set1)