import os, sys

status_dict = {
    'username': None,
    'status': False,
}
# 保存注册用户信息 格式为 用户名|密码|
register_path = os.path.join(os.path.dirname(__file__), 'db/register.txt')

# 获取用户密码
def get_user_pwd(username):
    try:
        users = {}
        with open(file=register_path, mode="r", encoding="utf-8") as r_f:
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
    with open(file=register_path, mode="r", encoding="utf-8") as r_f:
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

    with open(file=register_path, mode="a", encoding="utf-8") as w_f:
        w_f.seek(0, 2)
        w_f.write(f"{username}|{password}")
        w_f.write("\n")

def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
    :param f:
    :return:
    '''
    def inner(*args, **kwargs):
        # 访问函数前进行三次登陆认证
        flag = 3
        if status_dict['status']:
            ret = f(*args, **kwargs)
            flag = 0
            return ret
        else:
            print("请先登陆用户")
        # 第一次验证失败，继续验证2次
        while flag > 1:
            if status_dict['status']:
                ret = f(*args, **kwargs)
                return ret

            elif flag <= 1:
                print("超过认证次数")
            flag -= 1

    return inner

@auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')

@auth
def collections():
    print('欢迎访问收藏页面')

@auth
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




