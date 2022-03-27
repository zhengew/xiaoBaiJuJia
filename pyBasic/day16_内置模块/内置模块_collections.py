''' 内置模块 collections 容器类
collections 模块:

namedtuple(): 命名元组

defaultdict() : 默认值字典

Counter() : 计数器

'''
from collections import namedtuple, defaultdict, Counter

''' 1. namedtuple() '''
# Rectangle = (namedtuple("Rectangle_class", ["length", "width"]))
#
# r = Rectangle(10, 5)
# 通过属性访问元组的元素
# print(r.length, r.width)
# 通过索引的方式访问元素
# print(r[0], r[1])

'''
2. defaultdict
如果键值不存在，会默认被添加
'''
# 创建字典的方式
# d = defaultdict(int, name="andy", age = 10)
# print(d["name"])
# print(d["age"])
# print(d["addr"]) # {"addr":0} 也会被添加
# print(d)

# 自定义函数充当第一个参数:
# 要求不能有参数
# def f():
#     return "hello"
#
# d = defaultdict(f, name = "andy", age = 10)
# print(d["addr"])
# print(d)

'''
3. Counter : 计数器, 计算可迭代对象中元素个数
'''
c = Counter("aabbbcddddefg")
print(c)
print(c.most_common(3))