'''
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

''' 方式一 '''
# 栈和队列
# class QueueAndStack():
#     def __init__(self):
#         self.db = []
#     def put(self, item):
#         self.db.append(item)
#     def get(self):
#         return self.db.pop()
#
# # 队列
# class Queue(QueueAndStack):
#     def get(self):
#         return self.db.pop(0)
#
# # 栈 先进后出
# class Stack(QueueAndStack):
#     pass

''' 方式二 '''
# 栈和队列
class QueueAndStack():
    def __init__(self):
        self.db = []
    def put(self, item):
        self.db.append(item)
    def get(self):
        return self.db.pop() if self.index else self.db.pop(0)

# 队列
class Queue(QueueAndStack):
    def __init__(self):
        self.index = 0
        QueueAndStack.__init__(self)

# 栈 先进后出
class Stack(QueueAndStack):
    def __init__(self):
        self.index = 1
        QueueAndStack.__init__(self)


a = Queue()
s = Stack()
for i in range(10):
    a.put(i)
    s.put(i)
print(a.db)
print(a.get())
print(a.db)
print()
print(s.db)
print(s.get())
print(s.db)


