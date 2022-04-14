import queue    # 线程之间数据安全的容器队列
from queue import Empty # 不是内置的错误类型，而是queue模块中的错误
# q = queue.Queue(4)  # fifo 先进先出的队列
# # q.get()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print('5 done')
# q.put_nowait(5)
# q.put(5)

# try:
#     q.get_nowait() # _queue.Empty
# except Empty:pass
# print('队列为空，继续其他内容')


# # 栈
# from queue import LifoQueue # last in first out 后进先出 栈 （递归里看 三级菜单的例子）
# lq = LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# print(lq.get())
# print(lq.get())
# print(lq.get())

# 堆栈实现三级菜单 https://www.cnblogs.com/Eva-J/articles/7205734.html#_label4




# from queue import PriorityQueue # 优先级队列
#
# priq = PriorityQueue()
# priq.put((2, 'alex'))
# priq.put((1, 'wusir'))
# priq.put((0, 'tbjx'))
#
# print(priq.get())
# print(priq.get())
# print(priq.get())
