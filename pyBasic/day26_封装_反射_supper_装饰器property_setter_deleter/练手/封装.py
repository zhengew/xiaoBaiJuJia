# 狭义上的封装
    # 私有的三种情况
        # 不想让你看也不想让你改

# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.__pwd = pwd
#
# xb = User('alex', '123456')
# print(xb.__pwd) # AttributeError: 'User' object has no attribute '__pwd'

        # 可以让你看，但不让你改

# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.__pwd = pwd
#     def get_pwd(self):
#         return self.__pwd
# xb = User('alex', '123456')
# print(xb.get_pwd())
# print(xb.__dict__) # {'name': 'alex', '_User__pwd': '123456'}

        # 可以看也可以改，但是要求按照我的规则改

# import re
# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.__pwd = pwd
#     def get_pwd(self):
#         return self.__pwd
#
#     def change_pwd(self, newpwd): # 表示用户必须调用我们自定义的修改方式修改  私有+change方法实现
#         if re.match('[a-zA-Z]', newpwd):
#             self.__pwd = newpwd
# xb = User('alex', '123456')
# print(xb.get_pwd())
# xb.change_pwd('abadddaa')
# print(xb.get_pwd())


# 封装的语法
    # 私有的静态变量

# class User:
#     __Country = 'China' # 私有的静态变量
#     def func(self):
#         print(self.__Country)
#         # 私有的静态变量在了类的内部可以使用，自动把这句话所在类的名字添加到私有变量名前面
#         # print(self._User__Country)
#
# xb = User()
# # print(xb.__Country) # AttributeError: 'User' object has no attribute '__Country'
# print(User().func()) # China

    # 私有的实例变量
    # 私有的绑定方法

import hashlib
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd # 私有的实例变量

    def __get_md5(self): # 私有的绑定方法
        m = hashlib.md5(self.name.encode('utf-8'))
        m.update(self.__pwd.encode('utf-8'))
        return m.hexdigest()

    def get_pwd(self): # 通过 私有实例变量 + 私有的绑定方法,对外界间接隐藏私有变量
        return self.__get_md5()

xb = User('alex', '123456') # 94e4ccf5e2749b0bfe0428603738c0f9
print(xb.get_pwd())
print(xb.__dict__) # {'name': 'alex', '_User__pwd': '123456'}



