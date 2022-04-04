# 作业2
# 写一个自定义模块，里面有你自己实现的mypickle和myjson，我只需要给你传递一个参数 'pickle' 或者 'json',
# 那接下来就用 对应参数下的方法去 dump 或 load, (我感觉用到了归一化设计)

import MyJson
import MyPickle
import os
import sys
def read_write(arg):
    if arg == 'pickle':
        path = os.path.join(os.path.dirname(__file__), 'pickle.txt')
        return getattr(MyPickle.MyPickle(path), 'dump'), getattr(MyPickle.MyPickle(path), 'load')

    elif arg == 'json':
        path = os.path.join(os.path.dirname(__file__), 'json.json')
        return getattr(MyJson.MyJson(path), 'dump'), getattr(MyJson.MyJson(path), 'load')


class Student():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

def main():
    # s1 = Student('li', 15, '001')
    # s2 = Student('zhou', 14, '002')
    # print(read_write('pickle')[0](s1))
    # for i in read_write('pickle')[1]():
    #     print(i, i.name, i.age, i.id)

    a = [1, 3, 4]

    read_write('json')[0](a)
    ret = read_write('json')[1]()
    for i in ret:
        print(i)






if __name__ == '__main__':
    main()