# from Features import *
import hashlib
user_status = {
        'username': None,
        'log_status': False
    }


def wrapper(f):
    def inner(*args, **kwargs):
        if user_status['log_status']:
            ret = f(*args, **kwargs)
            return ret
        if log_in() == 'fail':
            return 'fail'
        else:
            ret = f(*args, **kwargs)
            return ret

    return inner


def register():
    i = 1
    '''用户注册'''

    with open('userinfo', mode='r', encoding='utf-8') as f1:
        dic = {line.strip().split("|")[0]: line.strip().split("|")[1] for line in f1}
    while i:
        uname = input('用户名(按Q或q退出):')
        if uname.upper() == 'Q':
            return False

        if len(uname) == len([x for x in uname if x >= 'a' and x <= 'z' or \
                    x >= 'A' and x <= 'Z' or x >= '0' and x <= '9']):
            i = 0
        else:
            print('用户名只能由字母数字组成!')

        for key in dic:
            if uname == key:
                print('用户名已存在')
                i = 1

    while 1:
        with open('userinfo', mode='r+', encoding='utf-8') as f1:
            pword = input('密码(按Q或q退出):')
            if pword.upper() == 'Q':
                return False
            if len(pword) >= 6 and len(pword) <= 12:
                f1.seek(0, 2)
                Md5 = hashlib.md5(uname[::2].encode('utf-8'))
                Md5.update(pword.encode('utf-8'))
                f1.write(f'{uname}|{Md5.hexdigest()}|{pword}\n')
                return True
            else:
                print('密码长度为6-12位')


def log_in():
    '''用户登录'''
    if user_status['log_status']:
        print('用户已登录若要切换用户请注销')
        return 0
    with open('userinfo', mode='r', encoding='utf-8') as f1:
        dic = {line.strip().split("|")[0]: line.strip().split("|")[1] for line in f1}
    i = 3
    while i:
        username = input('用户名:')
        password = input('密码:')
        Md5 = hashlib.md5(username[::2].encode('utf-8'))
        Md5.update(password.encode('utf-8'))
        if username in dic and Md5.hexdigest() == dic[username]:
            user_status['log_status'] = True
            user_status['username'] = username
            return True
        print('登陆失败')
        i -= 1
    return 'fail'


def write_text():
    import os
    while 1:
        text = input("请输入'文件名|文件内容':").strip()
        if '|' not in text:
            print('文章格式不正确!')
            continue
        title, content = text.split('|')
        with open(os.path.join(r'..\大作业2\file', title), mode='w',
                  encoding='utf-8') as f1:
            f1.write(f'文件名:{title}\n')
            f1.write(f'文件内容:\n')
            f1.write(content)

        return True


def import_file():
    import os
    while 1:
        index = input("请输入导入的md文件(不加后缀名):").strip()
        if not os.path.exists(f'{index}.md'):
            print('文件不存在!')
            continue
        with open(f'{index}.md', mode='r', encoding='utf-8') as f1,\
            open(os.path.join(r'..\大作业2\file', f'{index}.text'),
                 mode='w', encoding='utf-8') as f2:
            for line in f1:
                f2.write(line)

        return True


def logout():
    user_status['log_status'] = False
    user_status['username'] = None


@wrapper
def essay():
    name = user_status['username']
    dic = {
        '1': write_text,
        '2': import_file
    }
    print(f'欢迎{name}进入文章页面\n')
    print('1.写入内容\n2.导入md文件')
    choose = input('>>>')
    if dic.get(choose):
        ret = dic[choose]()
    else:
        print("输入有误")


@wrapper
def comment():
    import os
    name = user_status['username']
    pl = 0
    file = os.listdir(os.path.join(os.getcwd(), 'file'))
    dic = {str(key): value for key, value in enumerate(file, 1)}
    print(f'欢迎{name}进入评论页面')
    while 1:
        print('选择要评论的文章:')
        for i in dic:
            print(f'{i}.{dic[i]}')
        choose = input(">>>")
        if dic.get(choose):
            with open(os.path.join(r'..\大作业2\file', dic[choose]),
                      mode='r+', encoding='utf-8') as f1:
                for line in f1:
                    print(line, end='')
                print()
                while 1:
                    cment = input('输入评论:')
                    if not cment:
                        print('输入不能为空!')
                        continue
                    lst = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
                    for word in lst:
                        if word in cment:
                            cment = cment.replace(word, len(word) * '*')
                    f1.seek(0)
                    s = '-------------------------------------------------------'
                    for line in f1:
                        if s in line:
                            pl = 1
                            break
                    if pl == 0:
                        f1.seek(0, 2)
                        f1.write('\n')
                        f1.write('\n')
                        f1.write('评论区:\n')
                        f1.write('-------------------------------------------------------\n')
                        f1.write(f"     {user_status['username']}:\n")
                        f1.write(f'     评论内容:{cment}\n')
                        return True
                    elif pl == 1:
                        f1.seek(0, 2)
                        f1.write(f"     {user_status['username']}:\n")
                        f1.write(f'     评论内容:{cment}\n')
                        return True
        else:
            print('输入有误!')


@wrapper
def diary():
    name = user_status['username']
    print(f'欢迎{name}进入日记页面')


@wrapper
def collection():
    name = user_status['username']
    print(f'欢迎{name}进入收藏页面')


def quit_boke():
    return 'fail'


def boke():
    menu = {
        '1': log_in,
        '2': register,
        '3': essay,
        '4': comment,
        '5': diary,
        '6': collection,
        '7': logout,
        '8': quit_boke,
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
    while 1:
        print(m)
        choose = input('>>>')
        if menu.get(choose):
            ret = menu.get(choose)()
        else:
            print("输入有误")
            continue
        if ret == 'fail':
            return 0

boke()



