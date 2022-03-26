# 1. 请实现一个装饰器，限制该函数被调用的频率，如10秒一次（借助于time模块，time.time()）
# （面试题,有点难度，可先做其他）
# def wrapper(func):
#     sleepTime = 0
#     def inner(*args, **kwargs):
#         import time
#         nonlocal sleepTime
#         if time.time() - sleepTime >= 10:
#             ret = func(*args, **kwargs)
#             sleepTime = time.time()
#             return ret
#         else:
#             print("请求频繁!")
#     return inner
#
# @wrapper
# def login():
#     print("login...")
#
# while 1:
#     if input(">>>").upper() == "Q":
#         break
#     login()




#
# 2.请写出下列代码片段的输出结果：

# def say_hi(func):
#     def wrapper(*args,**kwargs):
#         print("HI")
#         ret=func(*args,**kwargs)
#         print("BYE")
#         return ret
#     return wrapper
#
# def say_yo(func):
#     def wrapper(*args,**kwargs):
#         print("Yo")
#         return func(*args,**kwargs)
#     return wrapper
# @say_hi # func = say_hi(func)
# @say_yo # func = sya_yo(func)
# def func():
#     print("ROCK&ROLL")
# func()

'''
HI
Yo
ROCK&ROLL
BYE
'''


#
# 3. 编写装饰器完成下列需求:
#
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
#     1,京东首页
#     2,京东超市
#     3,淘宝首页
#     4,淘宝超市
#     5,退出程序
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,
# 只要输入一次京东账号和密码并成功,则任意访问.
# 这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,
# 只要输入一次淘宝账号和密码并成功,则这两个函数都可以
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。

# 3. 编写装饰器完成下列需求:
#
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
#     1,京东首页
#     2,京东超市
#     3,淘宝首页
#     4,淘宝超市
#     5,退出程序
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,
# 只要输入一次京东账号和密码并成功,则任意访问.
# 这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,
# 只要输入一次淘宝账号和密码并成功,则这两个函数都可以
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。

# 创建账户数据
# jdUsers, taoBaoUsers
def saveUserInfos(filename):
    import os
    with open(file=os.path.dirname(os.path.dirname(__file__)) + rf"/files/{filename}", mode="a", encoding="utf-8") as f:
        username = input("username:")
        password = input("password:")
        f.seek(0,2)
        f.write(username+"|"+password+"\n")
        f.flush()
        f.close()

# 系统登陆状态
loginStatus = {
            "sys":"",
            "status":False
        }

# 装饰器
def wrappers(selec):
    def wrapper(func):
        def inner(*args, **kwargs):
            if selec.upper() == "JD":
                if loginStatus["status"] and loginStatus["sys"] == "JD":
                    ret = func(*args, **kwargs)
                    return ret

                if login("jdUsers"):
                    ret = func(*args, **kwargs)
                    loginStatus["status"] = True
                    loginStatus["sys"] = "JD"
                    return ret

            elif selec.upper() == "TM":
                if loginStatus["status"] and loginStatus["sys"] == "TM":
                    ret = func(*args, **kwargs)
                    return ret

                if login("taoBaoUsers"):
                    ret = func(*args, **kwargs)
                    loginStatus["status"] = True
                    loginStatus["sys"] = "TM"
                    return ret
            else:
                print("登陆失败!")
        return inner
    return wrapper


# 登陆验证
def login(filename):
    import os

    userinfos = {}
    with open(file=os.path.dirname(os.path.dirname(__file__)) + rf"/files/{filename}", mode="r", encoding="utf-8") as f:
        for info in f:
            userinfos.setdefault(info.strip().split("|")[0], info.strip().split("|")[1])
        f.close()
    username = input("username:")
    password = input("password:")
    if username not in list(userinfos.keys()) or password != userinfos[username]:
        print("登陆失败!")
        return False
    else:
        print("登陆成功!")
        return True


def init():
    infos = ['京东首页', '京东超市', '淘宝首页', '淘宝超市', '退出程序']
    for i in range(len(infos)):
        print(f"{i+1},{infos[i]}")
    return infos
@wrappers("JD")
def jdHome():
    print("login 京东首页")

@wrappers("JD")
def jdMarkey():
    print("login 京东超市")

@wrappers("TM")
def tianMaoHome():
    print("login 天猫首页")

@wrappers("TM")
def tianMaoMarkey():
    print("login 天猫超市")


def main():
    init()
    funcs = [jdHome, jdMarkey, tianMaoHome, tianMaoMarkey]
    try:
        selected = int(input("请选择:"))
        while selected:
            if 1 <= selected < 5:
                funcs[int(selected)-1]()
            elif selected == 5:
                print("退出程序")
                break
            selected = int(input("请选择:"))
    except Exception:
        print("输入错误!")

if __name__ == '__main__':
    main()