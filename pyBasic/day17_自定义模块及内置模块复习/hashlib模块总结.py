''' hashlib 加密模块
包含多种加密模块，MD5, sha1, sha256, sha512...

用途:
1.密码加密,不能以明文的形式存储密码
2.文件的校验， 整体一次加密结果与分段加密汇总的结果相同

用法：
1. 将bytes类型的字节，转化成固定长度的16进制数字组成的字符串
2. 不同的bytes利用相同的算法(md5)转化成的结果一定不同
3. 相同的bytes利用相同的算法(md5)转化成的结果一定相同
4. hashlib算法是不可逆的，(MD5被破解了)
'''

import hashlib

m = hashlib.md5(r'test'.encode('utf-8')) # 加盐之后再加密，避免相同密码被撞库破解
m.update('123456'.encode('utf-8'))
pwd = m.hexdigest()
print(pwd)