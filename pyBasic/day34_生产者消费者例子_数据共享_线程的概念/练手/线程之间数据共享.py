# 线程之间的数据共享，但数据时不安全的
from threading import Thread

num = 10

class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global num
        num -= 1

def main():
    t_lst = []
    for i in range(10):
        t = MyThread()
        t.start()
        t_lst.append(t)

    for t in t_lst:
        t.join()

    print(num) # 0
if __name__ == '__main__':
    main()