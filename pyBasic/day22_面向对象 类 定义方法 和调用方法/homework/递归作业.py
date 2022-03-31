'''
# sys
    # sys.path
    # sys.argv 在执行python脚本的时候，写在python之后的所有内容，形成了一个列表
    # sys.modules 查看已经加载到内存中的所有模块
# os
    # 和文件 文件夹相关的
    # 和工作目录相关的
    # 和执行操作系统命令相关的
    # .path系列

# logging
    # 排错 数据分析 操作审计
    # 普通的输出(文件/屏幕)
    # 切分日志(时间/空间)

# shutil
    # 和文件相关的内容

'''

# 递归练习
    # 遍历文件夹下的所有文件 -- 掌握
import os
def find_files(path):
    lst = os.listdir(path)
    for name in lst:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            print(abs_path)
        elif os.path.isdir(abs_path):
            find_files(abs_path)

# find_files(os.path.dirname(__file__))

    # 查看文件夹的总大小 -- 看懂并知道实现方法
def get_files_size(path):
    fileSizes = 0
    lst = os.listdir(path)
    for name in lst:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            fileSizes += os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            ret = get_files_size(abs_path)
            fileSizes += ret
    return fileSizes

# print(get_files_size(os.path.dirname(__file__)))

    # 斐波那契额数列练习 -- 会写
def fib(n, a=1, b=1): # 1 1 2 3 5 8 13 21
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a+b  # 此处 相当于 a = b, c= a+b
        return fib(n-1, a, b)

# print(fib(100))

# 生成器
# def fib2(n):
#     if n == 1:
#         yield 1
#     else:
#         yield from (1, 1)
#         a, b = 1, 1
#         while n > 2:
#             a, b = b, a + b
#             yield b
#             n -= 1
#
# for i in fib2(100):
#     print(i)

    # 三级菜单 -- 看懂并知道实现方法
        # 要求：输入 q 退出，外层函数打印 'wahaha'
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def show_menu(citys):
    while True:
        for name in citys:
            print(name)
        name = input('>>>')
        if citys.get(name):
            dic = citys.get(name)
            flag = show_menu(dic)
            print(flag)
            if not flag: return False
        elif name.upper() == 'B':
            return True
        elif name.upper() == 'Q':
            return  False

# show_menu(menu)
# print('wahh')

# 算法（用递归实现）
    # 二分查找 [1,2,3,4,5,6,7,8,9, 10, 27, 36m 46, 58, 69] - 有序列表
        # in index 从列表中找到一个值的位置
        # 实现上面的功能 -- 用代码实现 （今日作业）

# def find_num(lis, index):
#     length = len(lis)
#
#
# def main():
#     lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]
#     find_num(lis)
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
    # print(lis)
    size = 0
    for name in lis:
        # print(name[0], name[2])
        for file in name[2]:
            size += os.path.getsize(os.path.join(name[0], file))
    return size

def filesize2(path):
    lis = os.listdir(path)
    size = 0
    for name in lis:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            size += os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            ret = filesize2(abs_path)
            size += ret
    return size

# def main():
#     path = os.path.dirname(__file__)
#     print(filesize(path))
#     print(filesize2(path))

# if __name__ == '__main__':
#     main()
# 整理笔记思路
    # 学习的梗概
        # 主要内容
    # 新的概念
    # 新的模块
    # 新的单词
    # 面试题/逻辑性比较强的题