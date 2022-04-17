from gevent import monkey
monkey.patch_all() # 会重写time模块为
import gevent
import time

def func():
    print('start')
    time.sleep(1)
    print('end')

g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)
# g1.join() # 阻塞协程g1
# g2.join()
# g3.join()
gevent.joinall([g1, g2, g3]) # 将协程全部阻塞