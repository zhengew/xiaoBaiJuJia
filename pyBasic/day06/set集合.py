''' set 集合 '''

# 集合是可变的数据类型，集合中的元素不可变，所以集合不能用来当作字典中的key
# 集合可以快速去重，例如 list1 = [1,1,2,3] - > list2 = set(list1)
# 集合的 交集 interselection, 并集 union, 差集 difference, 反交集 symmetric_difference, 子集 issubset, 超集 issuperset

''' 创建集合 '''
set1 = set({1,2,3})
# print(set1, type(set1))
set2 = {3, 4, 5}
# print(set2, type(set2))
# 注意：set3 = {} 创建的是一个空字典，不是集合类型
set3 = {}
# print(set3, type(set3))
'''
{1, 2, 3} <class 'set'>
{3, 4, 5} <class 'set'>
{} <class 'dict'>
'''

''' 集合的增删 '''

# 增
# 1. add()
set1 = set({1,2,3})
set1.add("test")
# print(set1)
# set1.add([1,2]) # TypeError: unhashable type: 'list' 集合中的元素必须是不可变类型，可哈希

# 2. update
set1.update([4,5,6])
# print(set1)

# 删
# 1. remove() 元素必须在集合中存在，否则抛出 KeyError异常
# set1.remove(7) # KeyError: 7
set1.remove(6)
# print(set1)

# 2. pop() 随机删除一个元素
set1.pop()
# print(set1)

# 3. del 删除集合
# del set1
# print(set1) # NameError: name 'set1' is not defined

# 4. clear() 清空集合
# set1.clear()
# print(set1)

# 集合的 交并差，反交集，超集，子集
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# 交集 interselection
print(set1.intersection(set2))

# 并集 union
print(set1.union(set2))

# 差集 difference
print(set1.difference(set2))

# 反交集 symmetric_difference
print(set1.symmetric_difference(set2))

# 超集 issuperset
print(set1.issuperset(set2))

# 子集
print(set1.issubset(set2))

# 让集合变成不可变类型
set1 = frozenset(set1)
print(set1, type(set1)) # frozenset({1, 2, 3}) <class 'frozenset'>

''' enumerate '''
list1 = [1, 2, 3, 4]
for i in enumerate(list1):
    print(i)
'''
(0, 1)
(1, 2)
(2, 3)
(3, 4)
'''


for k, v in enumerate(list1):
    print(k, v, type(k), type(v))

