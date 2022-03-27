''' 内置模块 time
time模块三大对象:
时间戳
结构化时间对象(9大字段)
字符串（重要）

time.sleep() 线程睡眠时间 单位 秒

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

''' time 模块

'''

import time

# 时间戳：从时间元年(1970.1.1 00:00:00)到现在经过的秒数
# print(time.time(), type(time.time())) # 1648302976.9908748 <class 'float'>

'''
2.获取格式化时间对象:是9个字典组成的。 年月日时分秒 周 一年中的第几天 夏令时
# 默认是当前系统时间的时间戳
time.gmtime() # 返回 GMT 格林尼治时间
time.localtime() # 当地时间
'''
# print(time.gmtime())
# time.struct_time(tm_year=2022, tm_mon=3, tm_mday=26, tm_hour=14, tm_min=11, tm_sec=44, tm_wday=5, tm_yday=85, tm_isdst=0)

# print(time.gmtime(1)) # 时间元年过1秒后，对应的时间对像

# print(time.localtime())
#time.struct_time(tm_year=2022, tm_mon=3, tm_mday=26, tm_hour=22, tm_min=16, tm_sec=14, tm_wday=5, tm_yday=85, tm_isdst=0)

'''
3. 格式化时间对象和字符串之间的转换

1> 时间对象转化成时间字符串
strftime(format: str,t: Union[tuple[int, int, int, int, int, int, int, int, int], struct_time)
'''
s = time.strftime("%Y-%m-%d %H:%M:%S")
print(s) # 2022-03-26 22:26:40

'''
2> 时间字符串转换成时间对象
def strptime(string: str,format: str = ...)
'''
s = time.strptime("2022-03-26","%Y-%m-%d")
print(s)

'''
4. 时间对象 转换成时间戳
mktime(t: Union[tuple[int, int, int, int, int, int, int, int, int], struct_time, struct_time])
'''
# 时间对象
t1 = time.localtime() # 时间对象
t2 = time.mktime(t1) # 获取对应的时间戳
print(t2)

print(time.mktime(time.localtime())) # 1648305731.0

'''
5. 暂停当前进程，睡眠 xxx 秒
time.sleep(xxx)
'''
for i in range(5):
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    # 休眠一秒钟
    time.sleep(1)



