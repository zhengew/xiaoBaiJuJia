''' 内置模块 pickle
pickle :
将python中所有的数据类型，转换成字节串，序列化过程。
将字节串转换成python中数据类型，反序列化.

用法同 json

总结：
1.pickle 常用场景：和json一样,一次性吸入，一次性读取

2. json 和 pickle的区别：
json:
1> 不是所有的数据类型都可以序列化，例如 集合，结果是字符串。
2> 不能多次对同一个文件序列化
3> json数据可以跨语言

pickle:
1> 所有的python数据类型都可以序列化，结果是字节串。
2> 可以多次对同一个文件序列化
3> pickle数据不可跨语言
'''

import pickle
pickle.load
#
# bys = pickle.dumps([1, 2, 3])
# print(bys, type(bys)) # b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.' <class 'bytes'>
#
# bys = pickle.dumps((1, 2, 3))
# print(bys)
#
# res = pickle.loads(bys)
# print(res, type(res)) # (1, 2, 3) <class 'tuple'>

# 所有的数据类型，都可以进行数据化
# bys = pickle.dumps(set("abc"))
# res = pickle.loads(bys)
# print(res, type(res))

''' 2. 把pickle 序列化的内容写入到文件中 '''
# with open('c.txt', mode='ab') as f:
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
'''
3. 从文件中反序列化 pickle数据
'''
# with open("c.txt", mode="rb") as f:
#     for i in range(6): # EOFError: Ran out of input
#         res = pickle.load(f)
#         print(res, type(res)) # [1, 2, 3] <class 'list'>

