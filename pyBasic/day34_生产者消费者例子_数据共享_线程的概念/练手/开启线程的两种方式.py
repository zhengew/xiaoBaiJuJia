# 开启线程的两种方式 线程的常用方法 和属性

# from threading import Thread, current_thread, enumerate, activeCount
#
# def func():
#     print(current_thread(), current_thread().ident)
#
# def main():
#     t_lst = []
#     for i in range(10):
#         t = Thread(target=func, args=())
#         t.start()
#         t_lst.append(t)
#     for t in t_lst:
#         t.join()
#
#     print('线程都执行完了')
# if __name__ == '__main__':
#     main()


from threading import Thread, Lock, current_thread

class MyThread(Thread):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def run(self):
        print('姓名:%s, 年龄:%s, 线程id:%s' %(self.name, self.age, current_thread().ident))

def main():
    info = [('alex', 18), ('tbjx', 20), ('wusir', 21)]
    t_l = []
    for line in info:
        t = MyThread(line[0], line[1])
        t.start()
        t_l.append(t)

    for t in t_l:
        t.join()

if __name__ == '__main__':
    main()
