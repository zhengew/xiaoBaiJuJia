'''
# 数据结构
    # {} dict key - value  通过key找v非常快
    # [] list 列表 通过 index取值非常快
    # () 元组
    # {1,} 集合
    # 'sx' 字符串

# 队列的概念
# 不是python内置的：
    # Queue 队列：先进先出 FIFO (first in first out)
        # put 方法
        # get 方法
    # stack 栈: 后进先出 LIFO (last in first out )
        # put 方法
        # get 方法
    # 继承关系
        # 完成代码的简化
'''
class QueueStack:
    def __init__(self):
        self.db = []
    def put(self, data):
        self.db.append(data)

    def get(self):
        return self.db.pop() if self.index else self.db.pop(0) # 非0 即True

# 队列 先进先出
class Queue(QueueStack):
    def __init__(self):
        self.index = 0
        QueueStack.__init__(self)

# 栈 后近先出
class Stack(QueueStack):
    def __init__(self):
        self.index = 1
        QueueStack.__init__(self)



# s = Stack()
# s.put(10)
# s.put(11)
# r = s.get()
# print(r)

'''
# 自定义pickle，借助pickle模块来完成简化的 dump 和 load
    # pickle dump
        # 打开文件
        # 把数据dump到文件里

    # pickle load
        # 打开文件
        # 读数据

# 举例：
# 对象 = Mypickle('文件路径')
# 对象.load() 能拿到这个文件中所有的对象
# 对象.dump(要写入文件的对象)

'''

import pickle
class Mypickle:
    def __init__(self, path):
        self.path = path
        self.write_f = open(path, mode='ab')
        self.read_f = open(path, mode= 'rb')\

    def dump(self, obj):
        pickle.dump(obj, self.write_f)
        self.write_f.flush()

    def load(self):
        # 方式一
        # objs = [] # 这种方式，当文件特别大时，会很慢，因为先写入到列表里，再读取
        # while True:
        #     try:
        #         obj = pickle.load(self.read_f)
        #         objs.append(obj)
        #     except EOFError:
        #         break
        # return objs
        # 方式二 使用生成器
        while True:
            try:
                yield pickle.load(self.read_f)
            except EOFError:
                break


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

c1 = Car('奔驰E', 2100000)
c2 = Car('宝马E', 2200000)
c3 = Car('奔驰E', 2100000)
c4 = Car('宝马E', 2200000)
import os

p = Mypickle(os.path.join(os.path.dirname(__file__), '02mypickle.pickle'))
p.dump(c1)
p.dump(c2)

# 遍历生成器，读取对象
for i in p.load():
    print(i, i.name, i.price)