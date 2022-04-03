'''
# sys.argv 练习
    # 写一个脚本，在cmd里执行,完成文件的 复制，删除，重命名
    # python xxx.py  用户名 密码 cp 文件路径 目的地址
    # python xxx.py  用户名 密码 rm 文件路径
    # python xxx.py  用户名 密码 rename 文件路径 目的地址
    # 待完成
    # python xxx.py  用户名 密码 move 文件路径 目的地址
    # python xxx.py  用户名 密码 mkdir 文件路径 目的地址
    # 在这个基础上实现 move 移动，把一个文件或者文件夹移动到另一个位置
'''
import sys
import os

# print(sys.argv)
# python /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/02作业讲解_函数相关的.py alex sb cp 123 /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/user.txt /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/aaa

lis = ['/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/02作业讲解_函数相关的.py', 'alex', 'sb', 'cp', '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/aaa', '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day23/ddd']

import os
import shutil
import sys

# print(sys.argv)
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


# def main():
#     if len(sys.argv) > 5:
#         if login():
#             if sys.argv[3].lower() == 'cp' and len(sys.argv) == 6:
#                 if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
#                     filename = os.path.basename(sys.argv[4])
#                     path = os.path.join(sys.argv[5], filename)
#                     shutil.copy2(sys.argv[4], path)
#             elif sys.argv[3].lower() == 'rm' and len(sys.argv) == 5:
#                 if os.path.exists(sys.argv[4]):
#                     if os.path.isfile(sys.argv[4]):
#                         os.remove(sys.argv[4])
#                     else:
#                         shutil.rmtree(sys.argv[4])
#
#             elif sys.argv[3].lower() == 'rename' and len(sys.argv) == 6:
#                 if os.path.exists(sys.argv[4]):
#                     os.rename(sys.argv[4], sys.argv[5])
#     else:
#         print("您输入的命令无效!")
#
# if __name__ == '__main__':
#     main()

# sys.argv 练习
    # 写一个脚本，在cmd里执行,完成文件的 复制，删除，重命名
    # python xxx.py  用户名 密码 cp 文件路径 目的地址
    # python xxx.py  用户名 密码 rm 文件路径 目的地址
    # python xxx.py  用户名 密码 rename 文件路径 目的地址

# 练习 使用walk来计算文件夹的总大小
import os
def filesize(path):
    lis = os.walk(path)
    size = 0
    for name in lis:
        # print(name[0], name[2])
        for file in name[2]:
            size += os.path.getsize(os.path.join(name[0], file))
    return size


def main():
    path = os.path.dirname(__file__)
    print(filesize(path))


if __name__ == '__main__':
    main()