# 简单的队列
from multiprocessing import Queue, Process

def consumer(q):
    while True:
        ret = q.get()
        if ret: # 非0即True
            print(ret)
        else:
            break
def producer(q):
    for i in range(10):
        q.put('%stest'%i)

if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer, args=(q,))
    p1 = Process(target=producer, args=(q,))
    p1.start()
    c1.start()
    p1.join()
    q.put(None) # 生产者执行完以后，给消费者put(None) 停止消费