# 先进先出队列
from queue import Queue, Empty

q = Queue(4) # 指定队列长度为4

for i in range(4):
    q.put(i)

for i in range(5):
    try:
        print(q.get_nowait())
    except Empty:
        print('队列为空')