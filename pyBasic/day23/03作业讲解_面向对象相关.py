# 定义一个圆形，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10 的圆形
    # 计算圆形的面积
    # 计算圆的周长
import math

class Circle:

    def __init__(self, r):
        self.r = r

    def squar(self):
        return round(math.pi * self.r * self.r, 2)

    def perimeter(self):
        return round(math.pi * 2 * self.r, 2)

# r1 = Circle(5)
#
# r2 = Circle(10)
# print(r1.squar(), r1.perimeter())

# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别又不同的用户名和密码
    # 登陆成功后 才创建对象
    # 设计一个方法 修改密码 鉴权

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = mk_md5(password)


#md5值
def mk_md5(obj):
    import hashlib
    return hashlib.md5(obj.encode('utf-8')).hexdigest()

def get_users():
    users = {}
    with open('user.txt', mode='r', encoding='utf-8') as f:
        for i in f:
            users.setdefault(i.strip().split('|')[0], i.strip().split('|')[1].strip())
        f.close()
    return users

# 登陆成功 返回 True, 失败返回False
def login():
    username = input('用户名:').strip()
    password = input('密码:').strip()
    if username in list(get_users().keys()) and mk_md5(password) == get_users().get(username):
        return True
    else:
        return False

def creat_user(username, password):
    users = get_users()
    if login():
        if username not in list(users.keys()):
            with open('user.txt', mode='a', encoding='utf-8') as f:
                f.seek(0,2)
                f.write(username+'|'+mk_md5(password))
                f.write('\n')
                f.flush()
                f.close()
            return Users(username, password) # 返回 Users对象
        else:
            return "用户已存在"
    else:
        return "登陆失败，重新登陆"

# 修改密码鉴权
def update_pwd(username):
    import os
    password = input("请输入原密码:").strip()
    if username in list(get_users().keys()) and mk_md5(password) == get_users().get(username):
        get_users()[username] = mk_md5(input("请输入新密码:").strip())
        with open('user_n', mode='w', encoding='utf-8') as f:
            for k,v in get_users().items():
                f.seek(0,2)
                f.write(k+'|'+v)
                f.write('\n')
            f.flush()
            f.close()
        os.remove('user.txt')
        os.rename('user_n', 'user.txt')
    else:
        return '原密码输入错误!'



def main():
    p1 = creat_user('test4', '123456')
    print(p1)
if __name__ == '__main__':
    main()