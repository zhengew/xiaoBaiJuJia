''' 装饰器
# 1. 装饰器 定义: 在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。

# 2. 开放封闭原则
1> 对扩展是开放的
2> 对修改是封闭的
'''

'''
1. 最简单版本的装饰器:
举例:计算函数执行时间
'''
# import time
#
# def func():
#     time.sleep(3)
#     print("装饰器的开放封闭原则: 对扩展是开放的,对修改是封闭的。")
#
#
# def timmer(function):
#     def inner():
#         startTime = time.time()
#         function()
#         endTime = time.time()
#         print(f"此函数的执行效率为:{endTime-startTime}毫秒")
#     return inner
#
# func = timmer(func)
#
# func() # 此时 满足了开放和封闭原则，在未改变被装饰函数的源代码以及调用方式，还添加了计算执行时间的功能

'''
2. 带返回值的装饰器
'''
import time

def index():
    time.sleep(2)
    print("装饰器的开放封闭原则: 对扩展是开放的，对修改是封闭的。")
    return "访问成功"

# 带返回值的装饰器
def timer(func):
    def inner():
        startTime = time.time()
        yet = func() # 接收函数返回值
        endTime = time.time()
        print(f"此函数的执行效率为:{endTime - startTime}毫秒.")
        return yet
    return inner

index = timer(index)

# msg = index()
# print(msg)


'''
3. 被装饰的函数带参数的装饰器 利用 *args **kwargs
'''
import time

def index():
    time.sleep(2)
    print("欢迎访问博客园主页!")
    return "登陆成功"

def home(name):
    time.sleep(1)
    print(f"欢迎访问{name}主页!")
    return "登陆成功"

# 被装饰函数带参数 带返回值的装饰器
def timer(func):
    def inner(*args, **kwargs):
        startTime = time.time()
        yet = func(*args, **kwargs)
        endTime = time.time()
        print(f"此函数的执行效率为:{endTime - startTime}毫秒")
        return yet
    return inner

# index = timer(index)
# print(index())
#
# home = timer(home)
# print(home("gitub"))

'''
4. 标准版装饰器 
用 @ 符号代码 上面的 home = timer(home)

# 语法:
def wrapper(func):
    def inner(*args,**kwargs):
        # 执行被装饰函数之前的操作
        ret = func(*args, **kwargs)
        # 执行被装饰函数之后的操作
        return ret
    return inner
    
@wrapper

'''
# 举例:
import time

# 定义装饰器
def timer(func):
    def inner(*args, **kwargs):
        startTime = time.time()
        yet = func(*args, **kwargs)
        endTime = time.time()
        print(f"此函数的执行效率为:{endTime - startTime}毫秒")
        return yet

    return inner

@timer # 相当于 home = timer(home)
def home(name):
    time.sleep(1)
    print(f"欢迎访问{name}主页!")
    return "登陆成功"

# msg = home("github")
# print(msg)

'''
5. 带参数的装饰器, 其实就是嵌套

带参数的装饰器，参数可以传入多个，一般带参数的装饰器在以后的工作中都是给你提供的， 
你会用就行，但是自己也一定要会写，面试经常会遇到。
'''
# 举例：还是博客园登陆的案例

smteller = {
    'teller' : 'test1',
    'pwd' : '123',
    'status' : False,
}

# 模拟带删除的装饰器
def checking(x):
    def check(func):
        def inner(*args, **kwargs):
            if smteller["status"]:
                ret = func(*args, **kwargs)
                return ret

            if x == "wechat":
                username = input("用户名:").strip()
                pwd = input("密码:").strip()
                if username == smteller["teller"] and pwd == smteller["pwd"]:
                    smteller["status"] = True
                    ret = func(*args, **kwargs)
                    return ret
            elif x == "QQ":
                username = input("用户名:").strip()
                pwd = input("密码:").strip()
                if username == smteller["teller"] and pwd == smteller["pwd"]:
                    smteller["status"] = True
                    ret = func(*args, **kwargs)
                    return ret

        return inner
    return check


@checking("wechat")
def diary():
    print("欢迎访问日记页面!")

@checking("wechat")
def comment():
    print("欢迎访问评论页面!")

@checking("wechat")
def home():
    print("登陆成功,欢迎访问主页!")

diary()
comment()
home()

'''
@checking("wechat"):分两步：
    第一步先执行checking("wechat")函数，得到返回值 check
    第二步 @ 与 check 结合，形成 装饰器 @check 然后在依次执行。

这样就是带参数的装饰器，参数可以传入多个，一般带参数的装饰器在以后的工作中都是给你提供的， 你会用就行，但是自己也一定要会写，面试经常会遇到。
'''