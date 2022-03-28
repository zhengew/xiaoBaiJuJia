'''
序列化模块 (非常非常重要)
序列化:将一个数据结构(list,dict....)转化成一个特殊的序列(特殊的字符串)的过程.

1.为什么存在序列化?

数据 --> bytes
只有字符串和bytes可以互换.
数据存储在文件中,str(bytes类型)形式存储，比如字典;
数据通过网络传输(bytes类型)，str不能还原回去；
特殊的字符串: 序列化

2. 序列化模块
json 模块: 所有语言都支持
pickle 模块: 只能在python语言中使用

json序列化:
两对四个方法:
dumps,loads 主要用于网络传输,可以用于文件的存取.
'''
import json
'''
1. dumps loads 主要用于网络传输,但是也可以读写文件
'''
# dic = {'username':'太白', 'password': 123, 'status': True}
# 特殊的字符串
# st = json.dumps(dic, ensure_ascii=False)
# print(st, type(st))
# 反转回去
# dic1 = json.loads(st)
# print(dic1,type(dic1))

# 写入json文件
# l1 = [1, 2, 3, [4, 5, 6]]
# 1>转化成特殊的字符串写入文件
# with open('json.json', mode='a', encoding='utf-8') as f1:
#     f1.seek(0, 2)
#     f1.write(json.dumps(l1))
#     f1.write("\n")

# 2> 读取json文件中的特殊字符串，还原回来
# with open('json.json', mode='r', encoding='utf-8') as f2:
#     for i in f2:
#         l1 = json.loads(i)
#         print(l1, type(l1))

'''
2. dump load 只能写入文件，只能写入一个数据结构
'''
# 1>写入数据
# l1 = [1, 2, 3, [4, 5, 6]]
# with open('json文件1.json', mode='w', encoding='utf-8') as f:
#     json.dump(l1, f)

# 2>读取数据
# with open('json文件1.json', mode='r', encoding='utf-8') as f2:
#     l1 = json.load(f2)
#     print(l1, type(l1))

# 3> 一次写入或读取多个特殊数据怎么做？ 只能用 dumps 和 loads 实现
# dic1 = {"username":"alex"}
# dic2 = {"username":'zew'}

# with open('json文件1.json', mode='w', encoding='utf-8') as f1:
#     f1.write(json.dumps(dic1) + "\n")
#     f1.write(json.dumps(dic2) + "\n")

# with open('json文件1.json', mode='r', encoding='utf-8') as f2:
#     for i in f2:
#         l1 = json.loads(i)
#         print(l1, type(l1))

'''
pickle 
用法同 json, 只不过pickle转化成了字符串， json转换成了字符
'''
import pickle

# dic1 = {'name':'test1'}
# dic2 = {'name':'test2'}
# with open('pickle1.pickle', mode='wb') as f1:
#     f1.write(pickle.dumps(dic1))
#     f1.write(pickle.dumps(dic2))

# with open('pickle1.pickle', mode='rb') as f2:
#     for i in f2:
#         print(pickle.loads(i))



