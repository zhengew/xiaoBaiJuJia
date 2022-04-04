# 注册之后,重启所有的用户丢失
# 一次执行的注册行为,在之后所有执行中都能够正常登录
# 两个登录程序和面向对象的内容整理在一起,两个都要明白,都要记住

# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#
# class Account:
#     def __init__(self):
#         # 用户列表，数据格式：[user对象，user对象，user对象]
#         self.user_list = [] # 存储 User类实例化的对象
#
#     def login(self):
#         # 登录 输入用户名密码
#         # 和self.user_list作比对
#         uname = input('用户名:').strip()
#         passwd = input('密码:').strip()
#         for user in self.user_list:
#             if uname == user.name and passwd == user.pwd:
#                 print('登陆成功')
#             else:
#                 print('登陆失败')
#
#     def register(self):
#         # 注册成功了之后,user对象存在user_list里
#         uname = input('用户名:').strip()
#         passwd1 = input('密码:').strip()
#         passwd2 = input('密码确认:').strip()
#         if passwd1 == passwd2:
#             user = User(uname, passwd1)
#             self.user_list.append(user)
#             print('注册成功')
#         else:
#             print('注册失败,您两次输入密码不一致')
#
#
#     def run(self):  # 主程序里的判断逻辑用反射原理实现，作业 20220404
#         '''
#         主程序
#         :return:
#         '''
#         opt_lst = ['登陆', '注册']
#         while True:
#             for index, item in enumerate(opt_lst, 1):
#                 print(index, item)
#             num = input('请输入您需要的操作序号:').strip()
#             if num == '1':
#                 self.login()
#             elif num == '2':
#                 self.register()
#             elif num.upper() == 'Q':
#                 break


# if __name__ == '__main__':
#     obj = Account()
#     obj.run()

# 作业1
# 注册之后，重启所有的用户数据丢失
# 一次执行的注册行为，在之后所有执行中都能够正常登陆
# 两个登陆程序和面向对象的内容整理在一起，两个都要明白

# 作业2
# 写一个自定义模块，里面有你自己实现的mypickle和myjson，我只需要给你传递一个参数 'pickle' 或者 'json',
# 那接下来就用 对应参数下的方法去 dump 或 load, (我感觉用到了归一化设计)

class Foo(object):
     n1 = '吴佩奇'
     def __init__(self, name):
         self.n2 = name

obj = Foo('太白')
print(obj.n1)
print(obj.n2)

print(Foo.n1)
print(Foo.n2)

'''
Traceback (most recent call last):
  File "/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day26/登陆注册作业.py", line 75, in <module>
    print(Foo.n2)
AttributeError: type object 'Foo' has no attribute 'n2'
'''

