# hasattr 判断某一个类或对象能不能反射某个变量
# callable 判断某个反射的变量或内存地址，是不是可调用或可执行的
# getattr  通过字符串类型的名字，来操作这个名字对应的变量/对象/绑定方法等

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(f'我叫{self.age}, 今年{self.age}岁.')

alex = User('alex', 18)

if hasattr(alex, 'func'): # 判断 func 是否可以反射
    if callable(getattr(alex, 'func')): # 判断 func是否可调用
        getattr(alex, 'func')() # 如果可调用，就执行