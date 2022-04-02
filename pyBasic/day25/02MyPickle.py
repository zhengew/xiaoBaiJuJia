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