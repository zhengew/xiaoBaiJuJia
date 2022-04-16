# 优先级队列 PriorityQueue
# 接收的元素，可排序

from queue import PriorityQueue, Empty

q = PriorityQueue()

lst = [(1,'alex'), (2, 'tbjx'), (0, 'wusir')]
for i in lst:
    q.put(i)

for i in range(len(lst)):
    try:
        print(q.get_nowait())
    except Empty:
        print('优先级队列为空')

# (0, 'wusir')
# (1, 'alex')
# (2, 'tbjx')