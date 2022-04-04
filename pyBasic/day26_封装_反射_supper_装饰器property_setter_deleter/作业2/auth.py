class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print(f'{self.name} 过来吃饭了')
    def sleep(self):
        print(f'{self.name} 快睡觉')


# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容：（要求不能用异常处理）
    # 如果用户输入的是属性名，打印属性值
    # 如果输入的是方法名，调用方法
    # 如果输入的什么都不是，不做操作

def func():
    name = input('姓名: ').strip()
    age = input('年龄: ').strip()
    sex = input('性别: ').strip()
    obj = User(name, age, sex)

    while True:
        flag = input('>>>')
        if hasattr(obj, flag):
            if callable(getattr(obj, flag)):
                getattr(obj, flag)()
            else:
                print(getattr(obj, flag))


def main():
    func()

if __name__ == '__main__':
    main()