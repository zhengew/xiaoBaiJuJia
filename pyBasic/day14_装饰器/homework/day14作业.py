# 2. 读取register.txt 文件，模拟登陆博客园
def checking(x):
    def check(func):
        smteller = {}
        with open(file="..//files//register.txt", mode="r", encoding="utf-8") as read_f:
            for info in read_f:
                smteller.setdefault(info.strip().split("|")[0], info.strip().split("|")[1])

        def inner(*args, **kwargs):
            flag = 3
            if x == "wechat":
                while flag:
                    username = input("用户名:").strip()
                    password = input("密码:").strip()
                    if username not in list(smteller.keys()) or password != smteller[username]:
                        flag -= 1
                        if flag <= 0:
                            return False
                        print(f"用户名或密码错误，剩余次数:{flag}")
                    else:
                        ret = func(*args, **kwargs)
                        return ret
            elif x == "QQ":
                while flag:
                    username = input("用户名:").strip()
                    password = input("密码:").strip()
                    if username not in list(smteller.keys()) or password != smteller[username]:
                        flag -= 1
                        if flag <= 0:
                            return False
                        print(f"用户名或密码错误，剩余次数:{flag}")
                    else:
                        ret = func(*args, **kwargs)
                        return ret
        return inner
    return check

@checking("wechat")
def login(name):
    print(f"欢迎登陆{name}")

# login("github")

# 3.看代码写结果：
#
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
# @wrapper
# def func():
#     print(333)

# print(444)
# func()
# print(555)

'''
444
111
333
222
555
'''

# 4.编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。

# def decorator(func):
#     def inner(*args, **kwargs):
#         print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
#         ret = func()
#         return ret
#     return inner
#
# @decorator
# def index():
#     print("装饰器...")

# index()


# 5.为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def decorator(func):
#     def inner(*args, **kwargs):
#         try:
#             ret = func()
#             return ret + 100
#         except Exception:
#             return "返回值数据类型非 int , float"
#     return inner
#
# import random
# @decorator
# def func():
#     # return random.randint(1, 100)
#     return 7
# result = func()
# print(result)


# 6.请实现一个装饰器，通过一次调用是函数重复执行5次。
# def run(func):
#     def inner(*args, **kwargs):
#         for i in range(5):
#             ret = func(*args, **kwargs)
#     return inner
# @run
# def test():
#     print("通过装饰器，一次调用函数，重复执行5次")

# test()

# 7.请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
#
# 可用代码：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
#
# def wrapper():
#     pass
# def func1(f):
#     print(f.__name__)
# func1(wrapper)
# 函数名通过： 函数名.__name__获取。

# 装饰器
import time
def wrapper(func):
    def inner(*args, **kwargs):
        struct_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ret = func(*args, **kwargs)
        with open(file="..//files//funcName.txt", mode="a", encoding="utf-8") as writ_f:
            writ_f.seek(0,2)
            writ_f.write(func.__name__)
            writ_f.write("|")
            writ_f.write(struct_time)
            writ_f.write("\n")
        return ret
    return inner

@wrapper
def login():
    print("登陆成功!")

login()
