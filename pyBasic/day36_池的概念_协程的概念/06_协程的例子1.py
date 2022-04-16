# import gevent
#
# def func(): # 带有io操作的内容写在函数里，然后提交func给gevent
#     print('start func')
#     gevent.sleep(1)
#     print('end func')
#
# g1 = gevent.spawn(func)
# g2 = gevent.spawn(func)
# g3 = gevent.spawn(func)
# # g1.join()  # 阻塞，直到协程g1任务执行结束
# # g2.join()  # 阻塞，直到协程g1任务执行结束
# # g3.join()  # 阻塞，直到协程g1任务执行结束
# gevent.joinall([g1, g2, g3])


from gevent import monkey
monkey.patch_all()
import time
import gevent


def func(): # 带有io操作的内容写在函数里，然后提交func给gevent
    print('start func')
    time.sleep(1)
    print('end func')

g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)
# g1.join()  # 阻塞，直到协程g1任务执行结束
# g2.join()  # 阻塞，直到协程g1任务执行结束
# g3.join()  # 阻塞，直到协程g1任务执行结束
gevent.joinall([g1, g2, g3])