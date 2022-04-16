# 1.函数式编程
# from multiprocessing import Process
#
# def func(name, age):
#     print('姓名:%s, 年龄:%s'%(name, age))
#
#
# if __name__ == '__main__':
#     usr_l = [('alex', 18), ('大壮', 20), ('wusir', 21)]
#     for name, age in usr_l:
#         p = Process(target=func, args=(name, age))
#         p.start()

# 2.面向对象方式
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def run(self):
        print('姓名:%s, 年龄:%s' % (self.name, self.age))

if __name__ == '__main__':

    usr_l = [('alex', 18), ('大壮', 20), ('wusir', 21)]
    for name ,age in usr_l:
        p = MyProcess(name, age)
        p.start()
