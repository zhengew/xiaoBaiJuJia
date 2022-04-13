from multiprocessing import Process, Queue

def consumer(q):
    for i in range(10):
        print(q.get())

def producter(q):
    for i in range(10):
        q.put('hello %s' %i)

if __name__ == '__main__':
    q = Queue()

    p = Process(target=producter, args=(q,))
    p.start()
    p.join() # 异步阻塞 先生产在消费， 队列 put() 的数量如果小于get() 的数据会抛异常

    p = Process(target=consumer, args=(q,))
    p.start()
    p.join()