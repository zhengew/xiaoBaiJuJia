'''
# staticmethod装饰器
# 把一个普通的函数放到类中来使用，变成静态方法
# 静态方法既可以通过类名调用，也可以通过对象名来调用
'''

class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def login():
        print('这是一个静态方法，在函数内部没用到self和cls,在外部可以通过类名或对象名调用')

alex = User('alex')
User.login() # 通过类名调用静态方法
alex.login() # 通过对象名调用静态方法

