''' time 模块
线程睡眠时间 单位 秒  time.sleep()

1.时间戳 time.time()
2.时间对象 GMT: time.gmtime()  本地时间: time.localtime()
3.时间对象与字符串之间的相互转换 （常用）:
1> 时间对象转换成字符串
time.strftime(formart)
2> 字符串转换成时间对象
time.strptime(str, format)

4.时间对象与时间戳之间的相互转换
1> 时间对象转换成时间戳
time.mktime(time.localtime())
2>时间戳转换成时间对象
time.gmtime()  time.localtime()
'''

# 练习：
import time
# 时间戳
print(time.time())

# 时间戳与时间对象的相互转换
# 1> 时间戳->时间对象
gmt = time.gmtime()
local = time.localtime()
print(gmt, "\n", local)

# 2> 时间对象 -> 时间戳
t = time.mktime(time.localtime())
print(t)

# 时间对象与时间字符串的相互转换
# 1> 时间对象 -> 时间字符串
t1 = time.strftime("%Y-%m-%d %H:%M:%S")
print(t)
# 2> 时间字符串 -> 时间对象
t = time.strptime("2022-03-27 09:20:36", "%Y-%m-%d %H:%M:%S")
print(t)
print(time.strptime(t1, "%Y-%m-%d %H:%M:%S"))
