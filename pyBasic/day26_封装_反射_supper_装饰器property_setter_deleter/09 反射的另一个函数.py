class A:
    Role = '治疗'
    def __init__(self):
        self.name = 'alex'
        self.age = 84
    def func(self):
        print('wahaha')
        return 666
a = A()
# print(getattr(a, 'sex')) # AttributeError: 'A' object has no attribute 'sex'
# print(hasattr(a, 'sex'))
# print(hasattr(a, 'age'))
# print(hasattr(a, 'func'))
if hasattr(a, 'func'):  # 1. 判断某一个类或者某一个对象能不能反射某一个变量
    print(getattr(a, 'func'))
    if callable(getattr(a, 'func')): # 2. 如果能反射，还想要执行，还需要判断一下这个反射的变量或者内存地址是不是可调用或可执行的,如果是才能加括号
        getattr(a, 'func')()

# callable() 判断是否可调用
# print(callable(a.func))
# print(callable(a.age))
