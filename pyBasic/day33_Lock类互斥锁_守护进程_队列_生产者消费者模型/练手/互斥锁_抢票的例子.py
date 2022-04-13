import json
import time
from multiprocessing import Process, Lock

def search(i):
    with open('ticket', mode='r', encoding='utf-8') as f:
        ticket = json.load(f)
        print('%s:当前剩余%s张票' %(i, ticket['count']))

def buy_ticket(i):
    with open('ticket', mode='r', encoding='utf-8') as f:
        ticket = json.load(f)
    if ticket['count'] > 0:
        ticket['count'] -= 1
        print('%s 买到票了'%i)
    time.sleep(0.2)
    with open('ticket', mode='w', encoding='utf-8') as f:
        json.dump(ticket, f)

def get_ticket(i, lock):
    search(i)
    with lock: # 互斥锁，代替 lock.acquire() 和 lock.release()
        buy_ticket(i)

def main():
    lock = Lock()
    p_lst = []
    for i in range(10):
        p = Process(target=get_ticket, args=(i,lock))
        p.start()
        p_lst.append(p)

    for p in p_lst:
        p.join()


if __name__ == '__main__':
    main()