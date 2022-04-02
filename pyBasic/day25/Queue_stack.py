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



s = Stack()
s.put(10)
s.put(11)
r = s.get()
print(r)
# 假设你希望一个类的多个对象之间的某个属性是各自的属性，而不是共同的属性
# 这个时候我们要把变量存储在对象的命名空间中，不能建立静态变量
# 如果建立静态变量，是所有的对象共同使用一个变量