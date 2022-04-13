import random
import time
from multiprocessing import Process, Queue

# 消费者 通过外部条件控制消费者什么时候停止）
def consumer(q, name):
    while True: # 消费者 :通常取到数据之后还要进行某些操作
        food = q.get()
        if food:
            print('%s 开始吃%s'%(name, food))
        else:
            break

def producer(q, name, food):
    for i in range(10):
        foodi = '%s%s' %(food, i)
        print('%s生产了%s'%(name, food))
        time.sleep(random.random())
        q.put(foodi)


def main():
    q = Queue()
    c1 = Process(target=consumer, args=(q, 'alex'))
    c1.start()
    c2 = Process(target=consumer, args=(q, 'lc'))
    c2.start()
    p1 = Process(target=producer, args=(q, 'tbjx', '鸡蛋羹'))
    p1.start()

    p2 = Process(target=producer, args=(q, 'wusir', '大米粥'))
    p2.start()
    p1.join()
    p2.join()  # 当生产者都执行完毕后，向消费者提供终止消费的条件
    q.put(None)
    q.put(None)

if __name__ == '__main__':
    main()