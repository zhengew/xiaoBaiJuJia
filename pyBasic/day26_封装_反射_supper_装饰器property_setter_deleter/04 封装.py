''' 封装
# 封装：就是把属性或者方法装起来

# 广义：把属性和方法装起来，外面不能直接调用了,要通过类的名字来调用
# 狭义：把属性和方法藏起来，外面不能调用，只能在内部偷偷调用

# 给一个名字前面加上了双下划线的时候，这个名字就变成了一个私有的
# 所有私有的内容或者名字都不能在类的外部调用，只能在类的内部使用
'''
# 狭义：把属性和方法藏起来，外面不能调用，只能在内部偷偷调用

# class User:
#     def __init__(self, name, passwd):
#         self.name = name
#         self.__pwd = passwd  # 私有的实例变量/私有的对象属性
#
#     def get_pwd(self):      # 表示用户不能改，只能看  私有+某个get方法实现的
#         return self.__pwd
#     def change_pwd(self):   # 表示用户必须调用我们自定义的修改方式来进行变量的修改   私有 + change方法实现
#         pass # 修改密码的规则
#
# alex = User('alex', 'sbsbsb')
# # print(alex.__pwd) # AttributeError: 'User' object has no attribute '__pwd'
# print(alex.get_pwd())

# class User:
#     __Country = 'china' # 私有的静态变量
#     def func(self):
#         print(User.__Country) # 在类的内部可以调用

# print(User.Country)     # 报错 在类的外部不能调用
# print(User.__Country)   # 报错 # AttributeError: type object 'User' has no attribute 'Country'
# User().func() # china

import hashlib
class User:
    def __init__(self, name, passwd):
        self.user = name
        self.__pwd = passwd # 私有的实例变量

    def __get_md5(self): # 私有的绑定方法
        md5 = hashlib.md5(self.user.encode('utf-8'))
        md5.update(self.__pwd.encode('utf-8'))
        return md5.hexdigest()

    def getpwd(self):
        return self.__get_md5()

# alex = User('alex', 'sbsbsb')
# print(alex.getpwd())

# 所有的私有化都是为了让用户不在外部调用类中的某个名字
# 如果完成私有化，那么这个类的封装度就更高了，封装度越高，各种属性和方法的安全性也越高，但是代码越复杂
# class User:
#     __Country = 'China'  # 私有的静态变量
#     __role = '法师'       # 私有的静态变量
#     def func(self):
#         print(self.__Country)  # 在类的内部使用的时候，自动的把当前这句话所在的类的名字拼在私有变量前完成变形
#

''' 问题1:加了__双下划线的名字为啥不能从类的外部调用了？ 在私有属性前加了 _类名 '''
# print(User.__dict__)  # '_User__Country': 'China', '_User__role': '法师',
# print(User._User__Country) # 在类的外部根本不能定义私有的概念
# __Country - > '_User__Country': 'China'
# __role    ->  '_User__role': '法师'


''' 问题2:私有的内容能不能被子类使用呢？ 不能 '''
# class Foo(object):
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def func(self):
#         print('in Son')
# Son() # in Son

# 案例一
# class Foo(object):
#     def __init__(self):
#         self.__func()  # 此处实际是 self._Foo__func(), Son()实例化并调用init时，实际执行的是 self._Foo__func(), 所以最终打印的 in Foo
#
#     def __func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def __func(self):  # 此处实际是 self._Son__func()
#         print('in Son')
# Son() # in Foo

# 案例二
# class Foo:
#     def __func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def __init__(self):
#         self.__func()  # self._Son__func()
#
# Son() # AttributeError: 'Son' object has no attribute '_Son__func'


''' 问题3:在其他语言中的数据的级别都有哪些？python中有哪些？'''
# public 共有的  类内类外都能用，父类子类都能用             python支持
# protect 保护的  类内能用，父类子类都能用，类外不能用       python不支持
# private 私有的  本类的类内部都能用，其他地方都不能用       python支持

