'''
__call__
'''
# callable(对象)
# 对象() 能不能运行就是callable判断的事儿

class A:
    def __call__(self, *args, **kwargs):
        print('____')

# obj = A()
# print(callable(obj))
# obj() # 对象+括号 调用的是 __call__方法下面的逻辑

# A()()
# Flask框架的源码