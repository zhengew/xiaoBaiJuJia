# 1.整理今天笔记，课上代码最少敲3遍。
# 2.用列表推导式做下列小题

# 3.过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l = ['asdgf', 'qwe', 'zxcvbn', 123, 'ab']
# lis = [i for i in l if len(str(i)) >= 3]
# print(lis)

# 4.求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# tu = (tuple([i for i in range(6) if (i % 2) == 0]), tuple([j for j in range(6) if (j % 2) != 0]))
# print(tu)

# 5.求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# lst = [i[2] for i in M]
# print(lst)

# 6.求出50以内能被3整除的数的平方，并放入到一个列表中。
# lst = [i for i in range(50) if (i % 3) == 0]
# print(lst)

# 7.构建一个列表：['python1期', 'python2期', 'python3期', 'python4期',
# 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# lst = [f'python{i}期' for i in range(1, 11)]
# print(lst)

# 8.构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# lst = [(i, i+1) for i in range(6)]
# print(lst)

# 9.构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# lst = [i*2 for i in range(10)]
# print(lst)

# 10.有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1',
# '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# lst = [f'{j}{i}' for i, j in enumerate(l1)]
# print(lst)

# 11.有以下数据类型：
# x = {'name':'alex',
#      'Values':[{'timestamp':1517991992.94,'values':100,},
#                {'timestamp': 1517992000.94,'values': 200,},
#             {'timestamp': 1517992014.94,'values': 300,},
#             {'timestamp': 1517992744.94,'values': 350},
#             {'timestamp': 1517992800.94,'values': 280}],}
# 将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200],
# [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
#
# x = {'name':'alex',
#      'Values':[{'timestamp':1517991992.94,'values':100,},
#                {'timestamp': 1517992000.94,'values': 200,},
#             {'timestamp': 1517992014.94,'values': 300,},
#             {'timestamp': 1517992744.94,'values': 350},
#             {'timestamp': 1517992800.94,'values': 280}],}
# lst = [[i['timestamp'], i['values']] for i in x['Values']]
# print(lst)

# 12.用列表完成笛卡尔积
#
# 什么是笛卡尔积？ 笛卡尔积就是一个列表，列表里面的元素是由输入的可迭代类型的元素对构成的元组，
# 因此笛卡尔积列表的长度等于输入变量的长度的乘积。
#
#     a. 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
#
# colors = ['black', 'white']
# # sizes = ['S', 'M', 'L']
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# lst = [(i, j) for i in colors for j in sizes]
# print(lst)

#     b. 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
#
# l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......
# ('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]

# shape = ['spades', 'diamonds', 'clubs', 'hearts']
# num = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
# lst = [(i, j) for i in num for j in shape]
# print(lst)

#
#
# 13.简述一下yield 与yield from的区别。
# yield 通过next返回一个或多个值
# yield from 将可迭代元素作为迭代器的每一个结果返回


# 14.看下面代码，能否对其简化？说说你简化后的优点？
# def chain(*iterables):
#
#  for it in iterables:
#
#     for i in it:
#
#        yield i
#
# g = chain('abc',(0,1,2))
#
# print(list(g))  # 将迭代器转化成列表

# def chain(*iterables):
#     for it in iterables:
#         yield from it
# g = chain('abc',(0,1,2))
# print(list(g))
# 优点:少一个for

# 15.看代码求结果（面试题）：
# v = [i % 2 for i in range(10)]
# print(v)
#
# v = (i % 2 for i in range(10))
# print(v)
#
# for i in range(5):
#  print(i)
# print(i)
'''[0,1,0,1,0,1,0,1,0,1]'''
'''一个生成器地址'''
'''0'''
'''1'''
'''2'''
'''3'''
'''4'''
'''4'''
# 16.看代码求结果：（面试题）
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
#
# g2=(i for i in g1)
#
# print(list(g1))
# print(list(g2))
'''[0,1,2,3]'''
'''[]'''
# 17看代码求结果：（面试题）
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
#
# for n in [1,10]:
#     g=(add(n,i) for i in g)
# print(list(g))

'''20'''
'''21'''
'''22'''
'''23'''