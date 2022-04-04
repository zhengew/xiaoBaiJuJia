# 注册之后,重启所有的用户丢失
# 一次执行的注册行为,在之后所有执行中都能够正常登录
# 两个登录程序和面向对象的内容整理在一起,两个都要明白,都要记住
import os
import sys
import pickle

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = [] # 存储 User类实例化的对象

    def login(self):
        # 登录 输入用户名密码
        # 和self.user_list作比对
        uname = input('用户名:').strip()
        passwd = input('密码:').strip()
        with open(os.path.join(os.path.dirname(__file__), 'smteller.txt'), mode='rb') as f:
            while True:
                try:
                    user = pickle.load(f)
                    if uname == user.name and passwd == user.pwd:
                        print('登陆成功')
                        break
                except EOFError:
                    print('登陆失败')
                    break


    def register(self):
        # 注册成功了之后,user对象存在user_list里
        uname = input('用户名:').strip()
        passwd1 = input('密码:').strip()
        passwd2 = input('密码确认:').strip()
        if passwd1 == passwd2:
            user = User(uname, passwd1)
            self.user_list.append(user)
            print('注册成功')
            with open(os.path.join(os.path.dirname(__file__), 'smteller.txt'), mode='ab') as f:
                pickle.dump(user, f)
        else:
            print('注册失败,您两次输入密码不一致')


    def run(self):  # 主程序里的判断逻辑用反射原理实现，作业 20220404
        '''
        主程序
        :return:
        '''
        opt_lst = ['login', 'register']
        while True:
            for index, item in enumerate(opt_lst, 1):
                print(index, item)
            num = input('请输入您需要的操作序号:').strip()
            if num == '1' or num == '2':
                if hasattr(Account, opt_lst[int(num)-1]):
                    if callable(getattr(Account, opt_lst[int(num)-1])):
                        getattr(Account, opt_lst[int(num)-1])(self)

            elif num.upper() == 'Q':
                break
            else:
                print('输入数据异常')



if __name__ == '__main__':
    obj = Account()
    obj.run()

# 作业1
# 注册之后，重启所有的用户数据丢失
# 一次执行的注册行为，在之后所有执行中都能够正常登陆
# 两个登陆程序和面向对象的内容整理在一起，两个都要明白