'''
# 操作系统的历史
    # 多道操作系统
        # 遇到io操作就切换的
        # 提高cpu的利用率
        # 进程之间数据隔离
        # 时空复用：再同一个时间点上，多个程序同时执行着，一块内存条上存储了多个进程的数据

    # 分时操作系统
        # 时间分片
        # 时间片的轮转
    # 实时操作系统

# 进程
    # 是计算机中最小的资源分配单位：每一个程序在运行起来的时候需要给分配一些内存
    # 是一个运行的程序
    # 在操作系统中用pid来标识一个进程
# 线程
    # 是计算中能被cpu调度的最小单位：实际执行具体编译解释之后的代码的是线程，所以cpu执行的是解释之后的线程的代码
# 并行和并发
    # 并行（好）：多个cpu，各自在自己的cpu上执行多个程序
    # 并发：一个cpu,多个程序轮流执行

# 同步和异步
    # 同步：调用一个操作，要等待结果
    # 异步：调用一个操作，不等待结果

# 阻塞和非阻塞
    # 阻塞：cpu不工作
    # 非阻塞：cpu工作

# 同步阻塞：
    # input  sleep recv recvfrom
    # 同步阻塞代码实例
    def func(*args):
        count = 0
        n = input('>>>') # 阻塞代码
        for i in args:
            count += i
        return count

    a,b= 1, 2
    c = a + b
    d = func(a, b, c)
    print(d)

# 同步非阻塞：
    # ret = eval('1+2+3+4+5')
    # 同步非阻塞代码实例
    def func(*args):
        count = 0
        for i in args:
            count += i
        return count

    a,b= 1, 2
    c = a + b
    d = func(a, b, c)
    print(d)

# 异步非阻塞:(阻塞 blocking)

import socket
sk = socket.socket()
sk.setblocking(False) # 非阻塞
sk.bind(('127.0.0.1', 9000))
sk.listen()

while True: # BlockingIOError: [Errno 35] Resource temporarily unavailable
    try:
        conn, addr = sk.accept()
    except BlockingIOError:
        pass

# 异步阻塞

'''

