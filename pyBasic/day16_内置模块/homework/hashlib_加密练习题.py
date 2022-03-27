''' 稍后写一写
注册和登陆程序：
1.注册 登陆 退出
2.通过 hashlib.md5() 加密，验证账户登陆
'''

# 返回md5加密后的密码
def mk_md5(username, pwd):
    import hashlib
    m = hashlib.md5(fr"{username}".encode("utf-8"))
    m.update(fr"{pwd}".encode("utf-8"))
    return m.hexdigest()

def register():
    import os
    username = input("username:").strip()
    password = input("password:").strip()
    mdPwd = mk_md5(username, password)

    with open(file="mdpwd.txt", mode="a", encoding="utf-8") as write_f, open(file="mdpwd.txt", mode="r", encoding="utf-8") as read_f:
        users = []
        for line in read_f:
            users.append(line.strip().split("|")[0])
        if username in users:
            print("用户已注册!")
            read_f.close()
        else:
            write_f.seek(0,2)
            write_f.write(f"{username}|{password}|{mdPwd}")
            write_f.write("\n")
            write_f.flush()
            write_f.close()


def login():
    import hashlib
    username = input("username:").strip()
    password = input("password:").strip()
    userInfos = {}
    with open(file="mdpwd.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            userInfos.setdefault(line.split("|")[0], line.split("|")[2].strip())

    if mk_md5(username,password) == userInfos[username]:
        print("登陆成功")
    else:
        print("用户名或密码错误")

def main():
    while 1:
    # login()
        register()
        login()

if __name__ == '__main__':
    main()