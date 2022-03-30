''' 递归函数
RecursionError: maximum recursion depth exceeded while calling a Python object
递归的最大深度是1000层: 为了节省内存空间，不要让用户无限使用内存空间。
 1. 递归要尽量控制次数，如果需要很多层递归才能解决问题，不适合用递归解决
 2. 循环和递归的关系:
    # 递归不是万能的
    # 递归比起循环来说更占用内存

修改递归的最大深度
import sys
sys.setrecursionlimit(100000)


你的递归函数必须停下来，
递归函数是怎么停下来的？


递归核心思想：
 函数的调用
 函数的参数
 函数的返回值

递归函数要想结束，必须在函数内写一个ruturn，并且ruturn的条件必须是一个可达到的条件.
并不是函数中又return，return的结果就一定能够在调用函数的外层接收到
'''
# def func(count):
#     count += 1
#     print(count)
#     if divmod(count, 10) == (5, 3):return
#     func(count)
#
# func(1)
import os

'''
先写正则作业，再写递归
'''

''' 递归练习 '''
# 1. 计算阶乘 5! = 5*4*3*2*1
    # 循环
    # 递归
# def func(num):
#     if num == 1:
#         return num
#     else:
#         return num * func(num-1)

# res = func(5)
# print(res)

# 2. os 模块，查看一个文件夹下的所有文件，这个文件夹下面还有文件夹，不知道文件又多少层,不能用walk
def show_file(path):
    nane_lst = os.listdir(path)
    for name in nane_lst:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            print(name)
        elif os.path.isdir(abs_path):
            show_file(abs_path)
# show_file(path=os.path.join(os.path.dirname(__file__), 'dira'))

# 3. os 模块, 计算一个文件夹下所有文件的大小，这个文件夹下还有文件夹，不用用walk
def file_zize(path):
    size = 0
    name_lst = os.listdir(path)
    for name in name_lst:
        abs_path = os.path.join(path, name) # 当前的绝对路径
        if os.path.isfile(abs_path):
            # print(abs_path, os.path.getsize(abs_path))
            size += os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            ret = file_zize(abs_path) # 拿到返回值后size累加
            size += ret
    return size
ret = file_zize(path=os.path.join(os.path.dirname(__file__), 'dira'))
# print(ret)

# 4. 计算斐波那契数列（以后都用循环做）
    # 试一下 找第100个数
    # 1 1 2 3 5 8 13 - > 1+1=2,1+2=3,2+3=5 规律

# 慢
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(100))

# 快
def fib2(n, a=1, b=1):
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a + b
        return fib2(n-1, a, b)

# print(fib2(100))

# 生成器
def fib(n):
    if n == 1:
        yield 1
    else:
        yield from (1, 1)
        a,b = 1,1
        while n > 2:
            a, b = b, a + b
            yield b
            n -= 1
# import time
# for i in fib(2):
#     time.sleep(0.5)
#     print(i)

# 4. 三级菜单(可能是r级别)
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

def citys(menu):
    while True:
        for name in menu:
            print(name)
        key = input('>>>').strip()
        if menu.get(key):
            dic = menu[key]
            flag = citys(dic)
            if not flag: return False
        elif key.upper() == 'B':
            return True
        elif key.upper() == 'Q':
            return False

citys(menu)
print('wahh')
