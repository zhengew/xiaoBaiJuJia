import requests
from multiprocessing import Process, Queue

url_dic = {'cnblogs':'https://www.cnblogs.com/Eva-J/articles/9235899.html',
           'baidu': 'https://www.baidu.com',
           'q1ys' : 'http://www.q1ys.com/explore/dianying-dongzuo'}


def producer(name, url, q):
    ret = requests.get(url)
    q.put((name, ret.text))

def consmer(q):
    while True:
        tup =  q.get()
        if tup == None:break
        with open('%s.html'%tup[0], encoding='utf-8', mode='w') as f:
            f.write(tup[1])

if __name__ == '__main__':
    q = Queue()
    pl = []
    for key in url_dic:
        p = Process(target=producer, args=(key, url_dic[key], q))
        p.start()
        pl.append(p)

    Process(target=consmer, args=(q,)).start()

    for p in pl:
        p.join()
    q.put(None)




    # join n 个进程， n个进程必须都执行完才继续
    # for i in range(4): # 异步阻塞
    #     print(q.get())

# (3, 200)
# (4, 200)
# (2, 200)
# (1, 200)

# 同步阻塞
    # 调用函数必须等待结果\cpu不工作 - input sleep recv accept connect get
# 同步非阻塞
    # 调用函数必须等待结果\cpu工作  - 调用了一个高计算的函数 strip eval('1+2') sum min max sorted
# 异步阻塞
    # 调用函数不需要立即获取结果，而是继续做其他的事情，在获取结果的时候不知道先获取谁的，但是总之需要等(阻塞)
# 异步非阻塞
    # 调用函数不需要立即获取结果，也不需要等 start() terminate()


