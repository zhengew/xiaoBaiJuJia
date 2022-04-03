'''
# 自定义 json，借助 json 模块来完成简化的 dump 和 load
    # json dump
        # 打开文件
        # 把数据dump到文件里

    # json load
        # 打开文件
        # 读数据

# 举例：
# 对象 = Myjson('文件路径')
# 对象.load() 能拿到这个文件中所有的对象
# 对象.dump(要写入文件的对象)
'''
import os
import json
class MyJson:
    ''' 封装json 模块，实现文件中实例化对象的读和写 '''
    def __init__(self, path):
        self.path = path
        self.obj = []
    # 将对象分行写入文件
    def dump(self, obj):
        self.obj.append(obj)
        with open(self.path, mode='a', encoding='utf-8') as write_f:
            write_f.seek(0,2)
            write_f.write(json.dumps(obj)+'\n')
            write_f.flush()

    def load(self):
        with open(self.path, mode='r', encoding='utf-8') as read_f:
            for i in read_f:
                yield json.loads(i.strip())

class Student():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id



def main():
    path = os.path.join(os.path.dirname(__file__), 'myjson.json')
    s1 = [1, 2, 3, 4]
    s2 = {'name':'zew', 'age':30}

    # MyJson(path).dump(s1)
    # MyJson(path).dump(s2)

    for i in MyJson(path).load():
        print(i)

if __name__ == '__main__':
    main()