'''
pickle

'''

class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

python = Course('python', '6 month', 21800)
#
import pickle
# 利用 pickle.dump 将对象写到文件中
with open('pickle_file', 'wb') as f:
    pickle.dump(python, f)

# 利用 pickle.load 将对象读取出来，前提是 定义的类存在啊
with open('pickle_file', 'rb') as f:
    while True: # # EOFError: Ran out of input
        try:
            obj = pickle.load(f)
            print(obj.name, obj.period, obj.price)
            # print(ret)  # <__main__.Course object at 0x105350f70>
            # print(ret.__dict__)  # {'name': 'python', 'period': '6 month', 'price': 21800}
            # print(ret.name)
            # print(ret.price)
        except EOFError:
            break
