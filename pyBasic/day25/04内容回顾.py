''' 面向对象的回顾

# 类
class 类名:
    静态变量 = '值'
    def 函数(self):
        函数体
        pass
# 所有的变量和函数的地址都存储在类的命名空间里

# 对象
    # 对象 = 类名()

# 怎么用
    # 类能做什么？
        # 1.实例化对象
        # 2.操作静态变量

    # 什么时候是对 类中的 变量赋值，或者去使用类中的变量
        # 类名.名字 = '值'
        # print(类名.名字)
        # print(对象名.名字) # 如果对象本身没有这个名字

    # 什么时候是对 对象中 的变量赋值
        # 对象.名字的时候
        # self.名字的时候

# 所有的对象调用方法，就看这个对象是哪一个类的对象
# 不要担心多有的类的方法都是一样的名字，并不影响的
# 参考 类和对象的内空间分析截图

# 怎么继承？ 参考类和对象的内存空间， 把变量和在内存中是什么样子了解清楚，就吃透了

# class A:
#     lst = []
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(2)
#
# b = B()
# b.func()
# print(A.lst)  # []
# print(B.lst) # []

# 1 实例化B() 首先开辟空间 指向 b对象
# 2 调用 init方法，然后把 b 对象指向的内存空间作为参数传递给init中的 self, 然后 self.lst = [] 即在 b 对象空间中存在了 lst = []
# 3 b.func()  b对象通过类指针找到B类中的func(),执行 self.lst.append(2), 也就是往 b对象执行空间中的 lst 追加了一个2, lst = [2,]
# 4 print(A.lst)  A 类的lst 没有改变
# 5 print(B.lst)  B 类中没有 lst，通过类指针去父类A中找lst, 所以也打印[]

作业：
# 栈和队列的例子 默写
# Mypickle 仿照这个类写一个 Myjson(要求可以 dump多次， load多次)
# 所有的例子 把内存关系图画出来
'''
#
# class A:
#     role = []
#     def __init__(self):
#         self.l = []
#
#     def append(self, obj):
#         self.l.append(obj)
#
#     def pop(self, index = -1):
#         self.l.pop(index)
#
# print(A.role)
# a = A()

# class B:
#     def append(self):print('bbb')
#
# class C:
#     def append(self):print('ccc')
#
# b = B()
# d = C()
# b.obj = []
# b.obj.append(1) # b.obj = [1]


# b = B()
# b.append() # bbb  通过对象内存空间的 类指针 找到类中的append
# c = B()
# c.append() # bbb
# d.append() # ccc


# class B:
#     def append(self, value):
#         self.l.append(value)
#
# class C:
#     def append(self, value):
#         print('ccc')
#
# b = B()
# d = C()
# b.l = []
# b.append(10)
# print(b.l) # [10]

# class Queue:
#     def __init__(self):
#         self.lst = []
#
#     def append(self, value):
#         pass
#     def pop(self):
#         pass
#
# q = Queue()
# q.lst.append(10)  # lst = [10]
# q.append(5)
# print(q.lst) # [10]
# q.pop() # 空
# print(q.lst) [10]

# 注：
# 所有的对象调用方法，就看这个对象是哪一个类的对象
# 不要担心多有的类的方法都是一样的名字，并不影响的

''' 解析
# 怎么继承
'''
# 1. 案例1
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):print('b')
# A 是父类，B是子类
# 写代码的时候，是现有父类还是先有子类？
    # 在加载代码的过程中，需要先加载父类，所有父类写在前面
    # 从思考的角度出发，总是先把子类都写完，发现重复的代码，再把重复的代码放到父类中

# b = B()
# b.func() # b  子类有，不用父类的

# 2. 案例2
# class A:
#     def func(self):print('a')
# class B(A):pass
#
# b = B()
# b.func() # a  子类没有，用父类的

# 3. 案例3
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         A.func(self)
#         print('b')

# b = B()
# b.func() # a  b  先执行 B.func,调用了A.func打印a, 然后回到b.func 打印 b

# 4. 案例4
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         print('b')
#         A.func(self)
#
# b = B()
# b.func() # b a

# 5. 案例5
# class A:
#     lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     lst = []
#     def func(self):
#         self.lst.append(2)
#
# b = B()
# b.func()
# print(A.lst)  # []
# print(B.lst) # [2]

# 6. 案例6
# class A:
#     lst = [] # 静态变量
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def func(self):
#         self.lst.append(2)
#
# b = B()
# b.func()
# print(A.lst)  # [2]
# print(B.lst) # [2]


# 7. 案例7
# class A:
#     lst = []
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(2)
#
# b = B()
# b.func()
# print(A.lst)  # []
# print(B.lst) # []

# 1 实例化B() 首先开辟空间 指向 b对象
# 2 调用 init方法，然后把 b 对象指向的内存空间作为参数传递给init中的 self, 然后 self.lst = [] 即在 b 对象空间中存在了 lst = []
# 3 b.func()  b对象通过类指针找到B类中的func(),执行 self.lst.append(2), 也就是往 b对象执行空间中的 lst 追加了一个2, lst = [2,]
# 4 print(A.lst)  A 类的lst 没有改变
# 5 print(B.lst)  B 类中没有 lst，通过类指针去父类A中找lst, 所以也打印[]

# 栈和队列的例子 默写
# Mypickle 仿照这个类写一个 Myjson(要求可以 dump多次， load多次)
# 所有的例子 把内存关系图画出来