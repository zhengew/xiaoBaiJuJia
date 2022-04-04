class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        pass
    def sleep(self):
        pass


# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容：（要求不能用异常处理）
    # 如果用户输入的是属性名，打印属性值
    # 如果输入的是方法名，调用方法
    # 如果输入的什么都不是，不做操作