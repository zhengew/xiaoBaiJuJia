# __new__ 开辟内存空间
# 用来在 实例化类之前开辟一块空间，存储实例化对象
# supper().__new__(cls)

# 举例
class Clas:
    def __new__(cls, *args, **kwargs): # __new__ 开辟存储实例化对象的空间
        obj = super().__new__(cls)
        print('在init之前开辟存储对象的空间', cls)
        return obj # 把开辟的空间给 self
    def __init__(self):
        print('调用init', self)

# 实例化对象的三件事：
# 1. 首相在内存总开辟一块空间
# 2. 调用 __init__ 方法
# 3. 把 开辟的空间作为参数传递给 init方法的参数 self,
#    初始化参数并保存到开辟的对象空间中，这块空间指向了 实例化的对象
# c = Clas()
'''
在init之前开辟存储对象的空间 <class '__main__.Clas'>
调用init <__main__.Clas object at 0x10b440f10>
'''

# 单例模式
class Baby:
    __instance = None
    def __new__(cls, *args, **kwargs):
        # 如果cls.__instance 是None，就开辟空间，并返回给init,之后不再开辟空间
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, cloth, pants):
        self.cloth = cloth
        self.pants = pants

b1 = Baby('白衬衣', '黑裤子')     # 第一次开辟空间
print(b1.cloth, b1.pants)  # 白衬衣 黑裤子
b2 = Baby('紫T恤', '灰裤子')      # 第二次开辟空间
print(b1.cloth, b1.pants) # 紫T恤 灰裤子
print(b2.cloth, b2.pants) # 紫T恤 灰裤子