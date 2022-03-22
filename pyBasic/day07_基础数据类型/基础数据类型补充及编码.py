''' 字符串 '''
# name = "zheng er wei"
# 1. 首字母大写
# print(name.capitalize())

# 2. 大小写翻转
# print(name.swapcase())

# 3. 每个单词首字母大写
# print(name.title())

# 4.向内居中，空白处填充
# print(name.center(20, " "))

# 5.判断元素在字符串中是否存在,
# 5.1 find(value) # 返回找到元素的索引位置，如果不存在返回 -1
# index1 = name.find("er")
# print(index)

# 5.2 index(value) # 返回找到元素的索引位置，如果不存在抛异常 NameError
# index1 = name.index("er")
# print(index1)
# index2 = name.index("zew") # NameError: name 'index' is not defined

''' 元组 '''
# 1. 定义元组时，如果元组中只有一个1个元素且没有逗号，则该元组不是元组，类型为该元素本身的类型；如果有逗号，才是元组
# tup1 = (1)
# tup2 = (1,)
# print(type(tup1), type(tup2)) # <class 'int'> <class 'tuple'>

# 2. index() 返回元组中元素的索引位置，如果元素不存在，则抛出异常 ValueError
# tup1 = (1, 1, 2, 3)
# print(tup1.index(3))
# print(tup1.index(4)) # ValueError: tuple.index(x): x not in tuple

# 3. count() 返回元素在元组中出现的次数
# print(tup1.count(1))


''' 列表 '''
# list1 = [4, 1,1, 2, 3]
# 1. count() 统计列表中某个元素出现的次数
# print(list1.count(1))

# 2. index() 从列表中找出某个值第一个匹配项的索引位置
# print(list1.index(1))
# print(list1[1:].index(1))

# 3. sort() 正序, 参数 reverse = True 时，倒序排列
# list1.sort(reverse=True)
# list1.sort()
# print(list1)

# 4. reverse() 倒序
# list1.reverse()
# print(list1)

# 5. 列表可以做加法或乘法
# list2 = [1, 2, 3]
# list3 = [4, 5, 6]
# list2 += list3
# print(list2)
#
# list2 *= 3
# print(list2)

# 练习题
# 有列表l1, l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除

# l1 = [11, 22, 33, 44, 55]
# l2 = []
# for i in range(len(l1)):
#     if i % 2 != 0:
#         l2.append(l1[i])
# for j in l2:
#     l1.remove(j)
# print(l2, l1)

# 结论：在循环一列表的过程中，如果要改变列表的大小（增加或者删除元素），那么结果很可能会出错或者报错

''' 字典 '''
# 1. fromkeys() 创建一个字典，字典的所有key来自一个可迭代对象，字典的value来自同一个值
dic = dict.fromkeys([1, 2, 3], "test")
print(dic)

# 2. 练习题
# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除
dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}

list_keys = []
for key in dic.keys():
    if "k" in key:
        list_keys.append(key)

for key in list_keys:
    dic.pop(key)
print(dic)

# 总结：在循环字典的过程中，不能改变字典的大小（增删字典元素），否则会抛出运行时异常 RuntimeError

