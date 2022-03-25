'''
博客园登陆之后有几个页面，diary，comment，home，如果我要访问这几个页面，必须验证我是否已登录。
如果已经成功登录，那么这几个页面我都可以无阻力访问。
如果没有登录，任何一个页面都不可以访问，我必须先登录，登录成功之后，才可以访问这个页面。
我们用成功执行函数模拟作为成功访问这个页面，现在写三个函数，写一个装饰器，实现上述功能
'''

login_status = {
    'username': None,
    'status': False,
}

# 装饰器
def check(func):
    def inner(*args, **kwargs):
        if login_status["status"] == True:
            yet = func(*args, **kwargs)
            return yet
        loginName = input("用户名:").strip()
        password = input("密码:").strip()
        if loginName == "test1" and password == "123":
            login_status["status"] = True
            yet = func(*args, **kwargs)
            return yet
        else:
            return "用户名或密码错误,登陆失败"
    return inner

@check
def diary():
    print("欢迎访问日记页面!")

@check
def comment():
    print("欢迎访问评论页面!")

@check
def home():
    print("登陆成功,欢迎访问主页!")

diary()
comment()
home()