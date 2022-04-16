# 协程的原理
import time
def sleep(n):
    print('start sleep')
    yield time.time() + n
    print('end sleep')

def func(n):

    print(123)
    yield from sleep(n)   # 睡1s
    print(456)

def run_until_complete(g1,g2):
    ret1 = next(g1)
    ret2 = next(g2)
    time_dic = {ret1: g1, ret2: g2}
    while time_dic:
        min_time = min(time_dic)
        time.sleep(min_time - time.time())
        try:
            next(time_dic[min_time])
        except StopIteration:
            pass
        del time_dic[min_time]


n = 1
g1 = func(1)
g2 = func(1.1)
run_until_complete(g1,g2)