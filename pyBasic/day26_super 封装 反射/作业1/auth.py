class Authentic:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
    def register(self):
        pass
    def login(self):
        pass

#
l = [('登陆', 'login'), ('注册', 'register')]
# 循环这个列表
# 显示 序号 用户要的操作
# 用户输入序号
# 你通过序号找到对应的login或者register
# 先实例化
# 调用对应的方法，完成登陆或者注册功能