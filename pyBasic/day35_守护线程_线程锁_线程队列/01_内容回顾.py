'''
# 进程的生产者消费者模型(默写)
    # 多个进程访问网页
    # 一个进程负责把网页源码写到文件里
    # 消费者如何结束
    # 哪部分是生产者消费者模型比较重要的结构

# 数据共享
    # Manager  dict list 只要是共享的数据都存在数据不安全的现象
    # 需要我们自己加锁来解决数据安全问题

# 线程
    # 概念
        # 数据共享，效率高开销小，可以被多个cpu调度(是cpu调度的最小单位)，数据不安全，由操作系统负责调度
        # 在cpython解释器下：GIL锁 全局解释器锁，导致了同一个进程中的多个线程不能利用多核
    # 代码
        # thrading 模块
        # 对象 = 实例化：指定target args
            # start
            # join
            # ident
        # current_thread 能够获取当前这个函数所在的线程的线程对象
        # enmuerate
            # 导入之后会和内置模块enumerate重名，需要做特殊处理
            # from threading import enumerate as en # 别名
            # import threading
                # threading.enumerate()

        # active_count : 查看存活的线程个数(包括主线程)
'''