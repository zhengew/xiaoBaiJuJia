'''
创建字典
'''
# 方式一
dict_1 = dict([("one", 1), ("two", 2)])
# print(dict_1, type(dict_1))

# 方式二
dict_2 = dict(one=1, two=2)
# print(dict_2, type(dict_2))

# 方式三
dict_3 = dict({"one":1, "tow":2})
# print(dict_3, type(dict_3))

# 方式四 zip
dict_4 = dict(zip(["one", "two"], [1, 2]))
# print(dict_4, type(dict_4))

# 方式五 字典推导式
dict_5 = {key : value for key, value in [("one", 1), ("two", 2)]}
# print(dict_5, type(dict_5))

# 方式七 fromkey
dict_6 = dict.fromkeys("abc", "太白")
# print(dict_6, type(dict_6))

''' 验证字典的合法性 
# 字典的 key 必须是不可变类型，可哈希 int str tuple bool
# 字典的 value 可以是任意疏忽类型
'''

# key 类型不合法
# dic = {[1, 2, 3] : "abc"} # TypeError: unhashable type: 'list'
# print(dic)

''' 字典的增删改查 '''
dic = {"one" : 1, "two" : 2}

# 增
# 1.通过键值对增加
dic["three"] = 3
# print(dic)

# 2.setdefault(key, value)  有返回值，如果key存在,则不改变原value,若key不存在，则添加键值对
value = dic.setdefault("three", 4)
# print(value, dic)
# print(dic.setdefault("four", 4), dic)

# 删
dic1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# 1. pop(key) 通过key删除，有返回值，可设置返回值
value = dic1.pop("one", "None")
# print(value, dic1)
value = dic1.pop("five", "None")
# print(value, dic1)

# 2. popitem() 随机删除, 3.6版本以后为删除最后一个
dic1.popitem()
# print(dic1)

# 3. del dict[key] 通过key 删除键值对
del dic1["three"]
# print(dic1)

# 4. clear() 清空字典 dict.clear()
dic1.clear()
# print(dic1, type(dic1))

# 改
dic = {"one" : 1, "two" : 2}
# 1. 通过key直接改
dic["two"] = 3
# print(dic)

# 2. update

dict1 = {"one" : 1, "two" : 2}
dict2 = {"three" : 3, "four" : 4}
dict1.update(dict2)
# print(dict1, "\t", dict2)

dict1.update([(1, "a"), (2, "b")])
# print(dict1)

dict1.update(c = 3, d = 4)
# print(dict1)

# 查
dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# 1.通过key查询，如果key不存在则会提示 KeyError
# print(dict1["five"]) # KeyError: 'five'
# print(dict1["four"])

# 2.通过get查询，如果key不存在则返回 None，可设置默认返回值
value = dict1.get("five", "key不存在")
# print(value)

value = dict1.get("four", "key不存在")
# print(value)

# 3. keys() 遍历所有key, 类型为 dict_keys 的伪列表形式
values = dict1.keys() # dict_keys(['one', 'two', 'three', 'four']) <class 'dict_keys'>
print(values, type(values))
values = list(values)
print(values, type(values))

# 4. values() 遍历所有value
values = dict1.values() # dict_values([1, 2, 3, 4]) <class 'dict_values'>
print(values, type(values))

# 5. items() 遍历所有的键值对
values = dict1.items() # dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)]) <class 'dict_items'>
print(values, type(values))

for k,v in dict1.items():
    print(k,v)

# 结合 items() 及字典推倒式
dict2 = {k: v for k,v in (list(dict1.items()))}
print(dict2)
