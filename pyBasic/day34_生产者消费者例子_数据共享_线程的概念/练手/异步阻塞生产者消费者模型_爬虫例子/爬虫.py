# 异步阻塞
import requests
from multiprocessing import Process, Queue

url_dic = {'baidu':'https://www.baidu.com',
           'sina':'https://www.sina.com',
           'boc':'https://www.boc.cn/'}

def producer(q, name, url):
    ret = requests.get(url)
    ret.encoding = 'utf-8'
    q.put((name, ret.text))

def consumer(q):
    while True:
        ret = q.get()
        if ret:
            with open('%s.html'%ret[0], mode='w', encoding='utf-8') as f:
                f.write(ret[1])
        else:
            break

def main():
    q = Queue()
    p_lst = []
    for key in url_dic:
        p = Process(target=producer, args=(q, key, url_dic[key]))
        p.start()
        p_lst.append(p)

    Process(target=consumer, args=(q,)).start()

    for p in p_lst:
        p.join()

    q.put(None) # 有几个消费者就提供几个 None

if __name__ == '__main__':
    main()