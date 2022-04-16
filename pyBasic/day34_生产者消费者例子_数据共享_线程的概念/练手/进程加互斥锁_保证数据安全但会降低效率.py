# 锁：进程的互斥锁，必须拿到钥匙之后其他进程才能对数据进程修改，否则等待  原子性 一致性  持久性

# 抢票的例子 剩余一张票，多个进程去执行买票 扣减剩余票数的操作
from multiprocessing import Process, Lock
import json
def search():
    with open('ticket', 'r', encoding='utf-8') as f:
        ret = json.load(f)
        return ret

def buy_ticket(lock):

    with lock:
        ret = search()
        if ret['count'] > 0:
            ret['count'] -= 1
        with open('ticket', 'w', encoding='utf-8') as f:
            json.dump(ret, f)

if __name__ == '__main__':
    lock = Lock()
    p_l = []
    for i in range(10):
        p = Process(target=buy_ticket, args=(lock,))
        p.start()
        p_l.append(p)

    for p in p_l:
        p.join()
        # 多进程读同一个文件，是异步的，如果不加阻塞，一个进程在打开文件时，其他进程是不能同时操作文件的
        # FileNotFoundError: [Errno 2] No such file or directory
        # 仅仅是猜测， 反正 start() 是异步非阻塞， join是阻塞， 如果join了进程，主进程就必须等这个阻塞进程结束才能继续执行