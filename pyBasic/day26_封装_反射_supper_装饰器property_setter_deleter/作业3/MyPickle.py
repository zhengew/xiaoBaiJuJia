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
import os, sys
import pickle

class MyPickle:
    '''封装pickle模块，实现对象的读写'''
    def __init__(self, path):
        self.path = path

    def dump(self, obj):
        with open(self.path, mode='ab') as write_f:
            pickle.dump(obj, write_f)

    def load(self):
        with open(self.path, mode='rb') as read_f:
            while True:
                try:
                    yield pickle.load(read_f)  # 返回生成器
                except EOFError:
                    break

path = os.path.join(os.path.dirname(__file__), 'mypickle.txt')

class Student():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

def main():
    s1 = Student('li', 15, '001')
    s2 = Student('zhou', 14, '002')

    MyPickle(path).dump(s1)
    MyPickle(path).dump(s2)

    for i in MyPickle(path).load():
        print(i, i.__dict__)

if __name__ == '__main__':
    main()
