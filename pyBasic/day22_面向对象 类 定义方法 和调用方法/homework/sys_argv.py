'''
# sys.argv 练习
    # 写一个脚本，在cmd里执行,完成文件的 复制，删除，重命名
    # python xxx.py  用户名 密码 cp 文件路径 目的地址
    # python xxx.py  用户名 密码 rm 文件路径
    # python xxx.py  用户名 密码 rename 文件路径 目的地址
'''
import sys
import os
# print(sys.argv)
# python /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/02作业讲解_函数相关的.py alex sb cp 123 /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/user.txt /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/aaa

lis = ['/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/02作业讲解_函数相关的.py', 'alex', 'sb', 'cp', '123', '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/aaa', '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/ddd']

import os
import shutil
import sys

print(sys.argv)
#md5值
def mk_md5(obj):
    import hashlib
    return hashlib.md5(obj.encode('utf-8')).hexdigest()

def get_users():
    users = {}
    with open(os.path.join(os.path.dirname(__file__), 'user.txt'), mode='r', encoding='utf-8') as f:
        for i in f:
            users.setdefault(i.strip().split('|')[0], i.strip().split('|')[1].strip())
        f.close()
    return users

def login():
    username = input('用户名:').strip()
    password = input('密码:').strip()
    if username in list(get_users().keys()) and mk_md5(password) == get_users().get(username):
        return True
    else:
        return False


def main():
    if len(sys.argv) > 5:
        if login():
            if sys.argv[3].lower() == 'cp' and len(sys.argv) == 7:
                if os.path.exists(sys.argv[5]) and os.path.exists(sys.argv[6]):
                    filename = os.path.basename(sys.argv[5])
                    path = os.path.join(sys.argv[6], filename)
                    shutil.copy2(sys.argv[5], path)
            elif sys.argv[3].lower() == 'rm' and len(sys.argv) == 5:
                pass
            elif sys.argv[3].lower() == 'rename' and len(sys.argv) == 6:
                pass
    else:
        print("您输入的命令无效!")

if __name__ == '__main__':
    main()