from multiprocessing import Process, Manager, Lock

def change_dic(dic,lock):
    with lock:
        dic['count'] -= 1


if __name__ == '__main__':
    # m = Manager()
    with Manager() as m:
        lock = Lock()

        dic =  m.dict({'count':100})

        p_l = []

        for i in range(100):
            p = Process(target=change_dic, args=(dic,lock))
            p.start()
            p_l.append(p)

        for p in p_l: # 等待所有的进程都修改完闭
            p.join()

        print(dic)


# Manager 数据共享，但是数据有安全隐患，需要加锁