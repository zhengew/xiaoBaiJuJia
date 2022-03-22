''' 代码块和小数据池(不同代码块) '''
# id() 获取对象在内存中的地址
# == 比较数值是否相等
# is 比较对象在内存中的地址是否相等，如果内存地址相同，值一定相同

# 同一代码块中，int float str bool 都会被复用

# 不同代码块中，-5 ~ 256 中的数值默认保留在小数据池中
# a = 1
# b = 1
# c = 300
# d = 300
# print(a == b, a is b, id(a), id(b))
# print(c == d, c is d, id(c), id(d))

''' 将指定字符串驻留在小数据池中 '''
from sys import intern
# a = "hello##" * 20
# b = "hello##" * 20
# print(a == b, a is b, id(a), id(b))

# 总结：
'''
如果在同一代码块内，则采用同一代码块的缓存机制 int float str bool
如果在不同代码块内，则采用小数据池的驻留机制。 
from sys import intern 可将任意指定字符串添加到小数据池中，让其在内存中只创建一个对象，多个变量都指向着一个字符串。
'''

''' 深浅copy '''
# 1. 浅拷贝:在内存中重新开辟空间，但是内容还是沿用之前对象的内存地址
# 2. 深拷贝:在内存中重新开辟空间，原数据中可变的数据类型是重新创建的，不可变的数据类型是沿用之前的。

list1 = [1, "test", ["a", "b", "c"]]
# 浅拷贝
list2 = list1.copy()
print(id(list1), id(list2), id(list1[0]), id(list2[0]), id(list1[2]), id(list2[2]))

# 深拷贝
from copy import deepcopy
list3 = deepcopy(list1)
print(id(list1), id(list3), id(list1[0]), id(list3[0]), id(list1[2]), id(list3[2]))

# 面试题 浅kaobei
l1 = [1, 2, 3, 4, ['alex']]
l2 = l1[::]
l1[-1].append(666)
print(l2) # [1, 2, 3, 4, ['alex'， 666]]