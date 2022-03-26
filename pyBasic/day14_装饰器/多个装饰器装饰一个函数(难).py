''' 多个装饰器 装饰一个函数（没讲）'''
def func1(func):
    def inner1(*args, **kwargs):
        print("func1, before func")
        ret = func(*args, **kwargs)
        print("func1, after func")
        return ret
    return inner1


def func2(func):
    def inner2(*args, **kwargs):
        print("func2, before func")
        ret = func(*args, **kwargs)
        print("func2, after func")
        return ret
    return inner2

@func2 # login = func2(login) # 里面的login 相当于 inner1,外面的login相当于inner2
@func1 # login = func1(login) # 里面的login 相当于 inner2,外面的login相当于inner1
def logon():
    print("欢迎来到登陆页面!")

logon()