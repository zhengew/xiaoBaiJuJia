import hashlib
class Authentic:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
    def register(self):
        user = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        pwd2 = input('请确认密码: ').strip()
        if pwd == pwd2:
            with open('teller', mode='a', encoding='utf-8') as f:
                f.seek(0, 2)
                f.write(self.name+'|'+pwd+'\n')
                f.flush()
            print('注册成功!')
        else:
            print('两次秘密输入不一致!')


    def login(self):
        user = input('用户名: ').strip()
        password = input('密码: ').strip()
        if self.name == user and self.pwd == password:
            print('登陆成功')
            return True
        else:
            print('用户名或密码错误')
            return False




# 循环这个列表
# 显示 序号 用户要的操作
# 用户输入序号
# 你通过序号找到对应的login或者register
# 先实例化
# 调用对应的方法，完成登陆或者注册功能

import sys
def main():
    l = [('登陆', 'login'), ('注册', 'register')]
    while True:
        for k, v in enumerate(l):
            print(k, v[0])
        select = input('>>>').strip()
        if select == '0' or select == '1':
            if hasattr(sys.modules['__main__'], 'Authentic'):
                obj = Authentic('test1', '123456')
                if callable(getattr(obj, l[int(select)][1])):
                    getattr(obj, l[int(select)][1])()
        elif select.upper() == 'Q':
            print('退出程序')
        else:
            print('输入错误')





if __name__ == '__main__':
    main()