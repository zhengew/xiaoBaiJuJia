''' 带参数的装饰器
什么是装饰器？
为什么要又装饰器？
为什么不能改变原函数的调用方式？
    # 开放封闭原则
    # 我们提前写好一个功能，让别人使用的时候能够直接使用就能完成

# 登陆
# 计算函数的执行时间

# 写了很多的函数，
# 添加日志： 在X时间调用了什么函数

# 需求：
    登陆和注册的信息，写到 auth.log文件里
    所有的购物信息，写到operate.log里面
'''
import time
def logger(path):
    def log(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            with open(path, mode='a', encoding='utf-8') as f:
                msg = '%s 执行了%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), func.__name__)
                f.seek(0,2)
                f.write(msg+"\n")
                f.flush()
                f.close()
            return ret
        return inner
    return log

@logger('auth.log') # 函数只有调用时才会执行
def login():
    print('登陆逻辑')
@logger('auth.log')
def register():
    print('注册逻辑')
@logger('operate.log')
def show_goods():
    print('查看所有商品信息')
@logger('operate.log')
def add_goods():
    print('商品加入购物车')


def main():
    login()
    register()
    show_goods()
    add_goods()

if __name__ == '__main__':
    main()


# 带参数装饰器 练习:
# 又100个函数，分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有的时候不需要
# 希望能通过修改一个变量，能控制着100个函数的装饰器是否执行