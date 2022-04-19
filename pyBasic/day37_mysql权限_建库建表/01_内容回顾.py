# gil锁
    # 全局解释器锁,Cpython解释器下有的
    # 导致了python的多线程不能利用多核(不能并行)

# 内容回顾
# 池 concurrent.futures
    # 进程池 p = ProcessPoolExecutor(n)
    # 线程池 p = ThreadPoolExecutor(n)
    # future = submit 提交任务
        # future.result()获取结果
    # map 循环提交任务
    # add_done_callback 回调函数
# 协程
    # 协程:本质是一个线程
        #  能够在一个线程内的多个任务之间来回切换
        # 节省io操作的时间也只能是和网络操作相关的
        # 特点:数据安全,用户级别,开销小,不能利用多核,能够识别的io操作少
    # gevent 第三方模块  完成并发的socket server
        # 协程对象.spawn(func,参数)
        # 能识别的io操作也是有限的
        # 并且要想让gevent能够识别一些导入的模块中的io操作
        # from gevent import monkey;monkey.patch_all()
    # asyncio 内置模块
        # await 写好的asyncio中的阻塞方法
        # async 标识一个函数时协程函数,await语法必须用在async函数中
# import asyncio
# async def func():
#     print('sjkhaf')
#     await asyncio.sleep(1)
#     print('sjkhaf')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())
# loop.run_until_complete(asyncio.wait([func(),func(),func()]))


# 思维导图 -- 并发
    # 进程 :特点 操作模块 基础的方法和特点 IPC
    # 线程 : ***** GIL
    # 协程 : ***** 在爬虫的时候学到的模块都是基于协程实现的,flask框架/sanic框架
        # gevent
        # asyncio
    # 其他概念 : 同步异步 阻塞非阻塞 并发并行 调度算法 操作系统的发展

