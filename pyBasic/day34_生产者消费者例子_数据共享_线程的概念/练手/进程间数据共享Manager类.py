# 进程间的数据共享，但是有安全隐患
from multiprocessing import Process, Manager, Lock

def change_dic(dic, lock):
    with lock:
        dic['count'] -= 1

def main():
    with Manager() as m:
        lock = Lock()
        dic = m.dict({'count':1})
        p_lst = []
        for i in range(100):
            p = Process(target=change_dic, args=(dic, lock))
            p.start()
            p_lst.append(p)

        for p in p_lst:
            p.join() # 异步阻塞
            # 调用函数不需要立即获取结果，而是继续做其他事情，在获取结果时不知道先获取谁的，但是总之需要等(阻塞)
        print(dic)

if __name__ == '__main__':
    main()

# {'count': -91} 如果不加锁，
# 在其他进程做减法运算但没返回结果前，其他进程再去做减法运算，会少减去一次

# 加上互斥锁之后的结果：
# {'count': -99}  1 - 100 = -99
# 加锁可以保证数据安全，但会影响效率