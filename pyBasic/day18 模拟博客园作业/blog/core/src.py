import os, sys
from conf import  settings
from lib import common
status_dict = {
    'username': None,
    'status': False,
}


# 获取用户密码
def get_user_pwd(username):
    try:
        users = {}
        with open(file=settings.register_path, mode="r", encoding="utf-8") as r_f:
            for line in r_f:
                users.setdefault(line.strip().split('|')[0], line.strip().split('|')[1].strip())
        return users[username]
    except Exception:
        print("用户名或密码错误")

# 登陆
def login():
    username = input("用户名:")
    password = input("密码:")
    if password == get_user_pwd(username):
        status_dict['username'] = username
        status_dict['status'] = True
        return True
    else:
        return False
# 注册
'''
1.注册功能要求：
a.用户名、密码要记录在文件中。
b.用户名要求：只能含有字母或者数字不能含有特殊字符并且确保用户名唯一。
c.密码要求：长度要在6~14个字符之间。
'''
def register():
    users = {}
    with open(file=settings.register_path, mode="r", encoding="utf-8") as r_f:
        for line in r_f:
            users.setdefault(line.strip().split('|')[0], line.strip().split('|')[1].strip())
    username = input("用户名(只能含有字母或数字):")
    password = input("密码(6-14个字符):")

    while (not username.isalnum()) or username in list(users.keys()) or (len(password) < 6 or len(password) > 14):
        if not username.isalnum():
            username = input("用户名(只能含有字母或数字):")
        if username in list(users.keys()):
            username = input("用户名已存在，请重新输入:")
        if (len(password) < 6 or len(password) > 14):
            password = input("密码长度仅限(6-14个字符):")

    with open(file=settings.register_path, mode="a", encoding="utf-8") as w_f:
        w_f.seek(0, 2)
        w_f.write(f"{username}|{password}")
        w_f.write("\n")



@common.auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')

@common.auth
def comment():
    print('欢迎访问评论页面')

@common.auth
def dariy():
    print('欢迎访问日记页面')

@common.auth
def collections():
    print('欢迎访问收藏页面')

@common.auth
def login_out():
    status_dict['username'] = None
    status_dict['status'] = False
    print("退出登陆")

def quit():
    return "fail"

def run():
    menu = {
        '1': login,
        '2': register,
        '3': article,
        '4': comment,
        '5': dariy,
        '6': collections,
        '7': login_out,
        '8': quit,
    }
    m = \
        '''1.请登录
        2.请注册
        3.进入文章页面
        4.进入评论页面
        5.进入日记页面
        6.进入收藏页面
        7.注销账号
        8.退出整个程序'''.replace(' ', '')
    print(m)
    while 1:
        # print(m)
        choose = input('>>>')
        if menu.get(choose):
            ret = menu.get(choose)()
        else:
            print("输入有误")
            continue
        if ret == 'fail':
            return 0




