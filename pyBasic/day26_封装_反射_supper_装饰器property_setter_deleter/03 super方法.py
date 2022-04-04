# class A(object):
#     def func(self):
#         print('A')
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
# class D(B, C):
#     def func(self):
#         super().func()
#         print('D')
#
# D().func()

# mro() 顺序 D,B,C,A
# super 是按照mro顺序来寻找当前类的下一个类
# 在py3中不要传参数，自动就帮我们寻找当前类的mro顺序的下一个类中的同名方法
# 在pyt2中的新式类中，需要我们主动传递参数super(子类的名字,子类的对象).函数名()
# 这样才能够帮我们调用到这个子类的mro顺序的下一个类中的方法
# 在py2的经典类中，并不支持用super来找下一个类

# 在D类中找super的func,那么可以这样写 super().func()
# 也可以这样写 super(D, self).func(), (并且在py2的新式类中必须这样写)


# 在单继承的程序中，super就是找父类
class User:
    def __init__(self,name):
        self.name = name

class VIPUser(User):
    def __init__(self, name, level, start_date, end_date):
        # User.__init__(self,name)
        super().__init__(name)  # 单继承中推荐使用 super() 访问父类的方法， 本质上还是使用 mro() 方法
        # super(VIPUser, self).__init__(name)
        self.level = level
        self.start_date = start_date
        self.end_date = end_date


tb = VIPUser('tb', 6, '2022-03-22', '2022-04-03')
print(tb.__dict__)