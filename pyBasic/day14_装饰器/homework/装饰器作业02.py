# 1. 请实现一个装饰器，限制该函数被调用的频率，如10秒一次（借助于time模块，time.time()）
# （面试题,有点难度，可先做其他）
start_time = 0


def wrapper(f):
    import time
    def inner(*args, **kwargs):
        global start_time
        if (time.time() - start_time) >= 10:
            ret = f(*args, **kwargs)
            start_time = time.time()
            return ret
        else:
            print('你运行的太频繁啦!')

    return inner


@wrapper
def P_P():
    print('gogogogo')


while 1:
    if input('>>>') == "q":
        break
    P_P()
#
# 2.请写出下列代码片段的输出结果：
#
# def say_hi(func):
#     def wrapper(*args,**kwargs):
#         print("HI")
#         ret=func(*args,**kwargs)
#         print("BYE")
#         return ret
#     return wrapper
#
# def say_yo(func):
#     def wrapper(*args,**kwargs):
#         print("Yo")
#         return func(*args,**kwargs)
#     return wrapper
# @say_hi
# @say_yo
# def func():
#     print("ROCK&ROLL")
# func()
''' "HI" '''
''' "Yo" '''
''' "ROCK&ROLL" '''
''' "BYE" '''


#
# 3. 编写装饰器完成下列需求:
#
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
#
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
#
# 启动程序后,呈现用户的选项为:
#
#     1,京东首页
#
#     2,京东超市
#
#     3,淘宝首页
#
#     4,淘宝超市
#
#     5,退出程序
#
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,
# 只要输入一次京东账号和密码并成功,则任意访问.
# 这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,
# 只要输入一次淘宝账号和密码并成功,则这两个函数都可以
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
#
# user_status = {
#     'user': None,
#     'jingdong_log_status': False,
#     'taobao_log_status': False
# }
#
#
# def text_wrapper(n):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             import time
#             if user_status[f'{n}_log_status']:
#                 ret = f(*args, **kwargs)
#                 time.sleep(3)
#                 main()
#                 return ret
#             if log_in(n):
#                 ret = f(*args, **kwargs)
#                 time.sleep(3)
#                 main()
#                 return ret
#             else:
#                 print('访问失败')
#                 main()
#                 return False
#
#         return inner
#
#     return wrapper
#
#
# def log_in(n):
#     username = input('用户名:')
#     password = input('密码:')
#     f1 = open(f'{n}', mode='r', encoding='utf-8')
#     dic = {line.strip().split('|')[0]: line.strip().split('|')[1] for line in f1}
#     f1.close()
#     if username in dic and password == dic[username]:
#         user_status[f'{n}_log_status'] = True
#         return True
#     else:
#         return False
#
#
# @text_wrapper('jingdong')
# def jingdong_web():
#     print('京东首页')
#
#
# @text_wrapper('jingdong')
# def jingdong_mart():
#     print('京东超市')
#
#
# @text_wrapper('taobao')
# def taobao_web():
#     print('淘宝首页')
#
#
# @text_wrapper('taobao')
# def taobao_mart():
#     print('淘宝超市')
#
#
# def main():
#     func = [jingdong_web, jingdong_mart, taobao_web, taobao_mart]
#     while 1:
#         print(
#             '''1,京东首页
#     2,京东超市
#     3,淘宝首页
#     4,淘宝超市
#     5,退出程序
#             ''')
#         choose = input('>>>')
#         if choose >= '1' and choose <= '4':
#             func[int(choose) - 1]()
#         elif choose == '5':
#             return 0
#         else:
#             print('输入有误')
#
#
# main()