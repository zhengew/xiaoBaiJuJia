from multiprocessing import Lock,Process

def f(l,i):
    l.acquire()
    try:
        print("bob_",i)
    finally:
        l.release()


if __name__ == "__main__":
    lock = Lock()
    p_list = []
    for i in range(10):
        p = Process(target=f,args=(lock,i))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()
