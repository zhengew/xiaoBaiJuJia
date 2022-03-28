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

''' 加盐
动态的盐
'''
m = hashlib.md5(r'test'[::2].encode('utf-8')) # 'test'[::2] 动态的盐，盐是不固定的
pwd = m.hexdigest()
print(pwd)

''' sha系列   金融类，安全读比较高的行业用
随着数字越高，加密越复杂，越不易破解，但耗时越长。
'''
m = hashlib.sha256(r'test'.encode('utf-8')) # 加盐之后再加密，避免相同密码被撞库破解
m.update('123456'.encode('utf-8'))
pwd = m.hexdigest()
print(pwd)


''' 文件的校验

linux 中一切皆文件：文本文件，非文本文件，音频，视频，图片...
无论你下载的视频,还是软件(国外的软件),往往都会有一个md5值
'''

# 练习题：
# 通过分段加密下载文件，获取最终的加密字符串，校验官方提供的加密字符串是否相同，来判断文件是否被篡改过.