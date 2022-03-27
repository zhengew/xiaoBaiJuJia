''' 内置模块 JSON
json : JavaScript Object Notation: java脚本兑现标记语言,已经成为一种简单的数据交换语言.

序列化: 将内存中的数据，转换成字节串，用以保存在文件或通过网络传输，称为序列化过程。
反序列化: 从文件中或网络中获取的数据，转换成内存中原来的数据类型，称为反序列化过程。

json : 将数据转换成字符串，用于存储或网络传输。

json 总结:

1> 序列化
# json.dumps(obj)
# json.dump(obj,f)

2> 反序列化
# json.loads(s)
# json.load(f)


3>json文件通常一次性写，一次性读；使用另一种方式可以实现多次写，多次读
# 把需要序列化的对象，通过多次序列化的方式，用文件的write方式，把多次序列化后的json字符串写到文件中

with open(file = "json.txt", mode="w", encoding="utf-8") as f:
    f.write(json.dumps([1, 2, 3]) + "\n")
    f.write(json.dumps([4, 5, 6]) + "\n")


4> 把分次序列化的json字符串，反序列化回来

with open(file = "json.txt", mode="r", encoding="utf-8") as f:
    for i in f:
        print(json.loads(i.strip()))
'''

'''
# 1>
# t - > text
# b -> binary
# a -> append
# w -> write
# r - > read
# 默认是rt
# with open(file="a.txt", mode="wt", encoding="utf-8") as f:
#     f.write("a")
#     f.write([1,2]) # TypeError: write() argument must be str, not list
'''

import json

'''
1. json.dumps(obj) # 把指定的对象，转换成json格式的字符串
'''
# s = json.dumps([1,2,3])
# print(type(s)) # <class 'str'>
# print(s) # '[1, 2, 3]'

# a> 元组序列化后，变成字符串列表
# s = json.dumps((1, 2, 3))
# print(s) # [1, 2, 3]
#
# res = json.dumps(10)
# print(res, type(res)) # 10 <class 'str'>
#
# res = json.dumps({"name":"zew", "age":10})
# print(res, type(res)) # {"name": "zew", "age": 10} <class 'str'>

# res = json.dumps(set("abc")) # TypeError: Object of type set is not JSON serializable

'''
2. json.jdump(obj: Any,fp: IO[str]) :将json结果写到文件中
'''
# with open(file="a.txt", mode="at", encoding="utf-8") as f:
#     json.dump([1,2,3], f)


'''
3. json.loads() 反序列化
'''
# 注: 元组经过序列化，再反序列化，转成的类型是列表
# res = json.dumps((1, 2, 3)) # 序列化
# lst = json.loads(res) # 反序列化
# print(lst, type(lst)) # [1, 2, 3] <class 'list'>

'''
4. json.load() 从文件中反序列化
'''
# with open(file="a.txt", mode="rt", encoding="utf-8") as f:
#     res = json.load(f)
#     print(res, type(res)) # [1, 2, 3] <class 'list'>


'''
5.json文件通常一次性写，一次性读；使用另一种方式可以实现多次写，多次读
# 把需要序列化的对象，通过多次序列化的方式，用文件的write方式，把多次序列化后的json字符串写到文件中
'''
with open(file = "json.txt", mode="w", encoding="utf-8") as f:
    f.write(json.dumps([1, 2, 3]) + "\n")
    f.write(json.dumps([4, 5, 6]) + "\n")

'''
6. 把分次序列化的json字符串，反序列化回来
'''
with open(file = "json.txt", mode="r", encoding="utf-8") as f:
    for i in f:
        print(json.loads(i.strip()))