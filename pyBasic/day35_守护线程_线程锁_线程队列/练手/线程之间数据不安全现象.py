from threading import Thread

num =0

def add():
    for i in range(200000):
        global num
        num += 1

def sub():
    for i in range(200000):
        global num
        num -= 1

if __name__ == '__main__':
    t1 = Thread(target=add)
    t1.start()
    t2 = Thread(target=sub)
    t2.start()

    t1.join()
    t2.join()

    print(num) # -134151  对于赋值操作，只要赋值之前GIL锁切换了，就存在数据不安全问题