''' 反射的使用场景 '''
''' 1. 反射对象的实例变量 '''
''' 2. 反射类的 静态变量/绑定方法/其他方法 '''
''' 3. 模块中的所有变量
        # 被导入的模块      
        # 当前模块的py文件  - 脚本
'''

# class A:
#     Role = '法师'
#     def __init__(self):
#         self.name = 'alex'
#         self.age = 84
#     def func(self):
#         print('wahaha')
#         return 666
# a = A()
# print(getattr(a, 'name')) # 反射对象的实例变量
# print(getattr(a, 'func')()) # 反射对象的绑定方法
# print(getattr(A, 'Role'))  # 反射类中的静态变量
#
# import a # 引用模块中的任意的变量
# print(getattr(a, 'sww'), a.sww)
# getattr(a, 'sww')()
# print(getattr(a, 'lst'), a.lst)
# print(getattr(a, 'dic'), a.dic)
# print(getattr(a, 'we'), a.we)

import sys # 反射本模块中的内容
cat = '小a'
dog = '小b'
def pig():
    print('小p')
print(getattr(sys.modules['__main__'], 'cat'))
print(getattr(sys.modules['__main__'], 'dog'))
getattr(sys.modules['__main__'], 'pig')()