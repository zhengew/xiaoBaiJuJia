# 1. 写一个注册登陆 基于数据库来做
    # 加上 hashlib密文验证
# 2. 另外10道题

import pymysql
import hashlib
import sys

def db():
    try:
        conn = pymysql.connect(user='root',
                password='123456',
                host='172.16.238.4',
                database='day42',)

        return conn
    except Exception as e:
        return e

def get_md5(username, password):
    m = hashlib.md5(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def register(username, password):
    conn = db()
    try:
        cur = conn.cursor()
        pwd = get_md5(username, password)
        cur.execute("insert into teller values(null, %s, %s)", (username, pwd))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        return e

def login(username, password):
    conn = db()
    try:
        cur = conn.cursor()
        ret = cur.execute("select username, password from teller where username = %s", (username,))
        ret = cur.fetchone()
        if ret:
            uname, pwd = ret
            password = get_md5(username,password)
            if username == uname and password == pwd:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return e

def main():
    opt_list = [('注册', 'register'), ('登陆', 'login')]
    for index, opt in enumerate(opt_list, 1):
        print(index, opt[0])
    n = int(input('请选择:').strip())
    if hasattr(sys.modules[__name__], opt_list[n-1][1]):
        name = input('用户名:').strip()
        pwd = input('密码:').strip()
        ret = getattr(sys.modules[__name__], opt_list[n-1][1])(name, pwd)
        print(ret)

if __name__ == '__main__':
    main()