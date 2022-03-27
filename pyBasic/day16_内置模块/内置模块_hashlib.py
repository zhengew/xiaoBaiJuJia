''' 内置模块 hashlib
hashlib : 封装一些用于加密的类
md5(), ...

加密的目的: 用于判断和验证,而并非解密.
特点:
1> 把一个大的数据，切分成不同块，分别对不同块进行加密，再汇总结果，和直接对整体数据加密的结果是一致的.
2> 单项加密，不可逆.
3> 原始数据的一点小的变化，将导致结果的非常大的差异，'雪崩'效应.
'''
import hashlib


'''
md5 加密算法:

给一个数据加密的三大步骤:
1. 获取一个加密对象
2. 使用加密对象的update，进行加密; update可以调用多次
3. 通常通过 hexdigest 获取加密的结果，或者 digest()
'''

import hashlib

# 1. 获取一个加密对象
# m = hashlib.md5()

# 2. 使用加密对象的update，进行加密; update可以调用多次
# m.update('abc中文'.encode('utf-8'))
# m.update('def'.encode('utf-8'))

# 3.通过 hexdigest 获取加密的结果
# res = m.hexdigest()
# print(res) # 1af98e0571f7a24468a85f91b908d335

# 给一个数据加密:
# 验证: 用另一个数据加密的结果和第一次加密的结果对比。
# 如果结果相同，说明原文相同；如果不相同，说明原文不同.

'''
不同加密算法，实际上就是加密结果的长度不同
'''
# print(len(hashlib.sha224().hexdigest())) # 56
# print(len(hashlib.md5().hexdigest())) # 32

''' 加盐
在创建加密对象时，可以指定参数，称为 salt(盐)
'''
# m = hashlib.md5(b"abc")
# print(m.hexdigest())

# m = hashlib.md5()
# m.update(b"abc")
# print(m.hexdigest())

# 验证:把一个大的数据，切分成不同块，分别对不同块进行加密，再汇总结果，和直接对整体数据加密的结果是一致的.
# m = hashlib.md5()
# m.update(b"abcdef")
# print(m.hexdigest())
#
# m = hashlib.md5()
# m.update(b"abc")
# m.update(b"def")
# print(m.hexdigest())

''' 稍后写一写
注册和登陆程序：
1.注册 登陆 退出
2.通过 hashlib.md5() 加密，验证账户登陆
'''

