'''
__new__
'''

# class A:
#     def __new__(cls, *args, **kwargs): # 构造方法
#         # o = super().__new__(cls) # 方式一  super() 指向的就是object
#         o = object.__new__(cls) # 方式二
#         print('执行new', o)
#         return o
#
#     def __init__(self):
#         print('执行init', self)
#
# A()
# 执行new <__main__.A object at 0x1006f1f10>
# 执行init <__main__.A object at 0x1006f1f10>

# 实例化的时候
# 先创建一块对象的空间，有一个指针能指向类 -> __new__
# 调用init -> __init__

''' 设计模式 -- 单例模式 '''
# 一个类 从头到尾 只会创建一次self的空间

class Baby:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, cloth, pants):
        self.cloth = cloth
        self.pants = pants

b1 = Baby('红毛衣', '绿皮裤')
b2 = Baby('白衬衫', '黑豹纹')
print(b1, b2) # <__main__.Baby object at 0x10bb45f10> <__main__.Baby object at 0x10bb45f10>
print(b1.cloth, b2.cloth) # 白衬衫 白衬衫

from 单例 import baby  # 在py中一个模块的导入，永远只导入一次(单例模式)
