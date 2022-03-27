''' 内置模块 datetime
封装了一些和日期时间想过的类

date 类 : 年月日
time 类: 时分秒
datatime 类: 年月日时分秒，主要用于数学计算.
timedelta 类：时间计算的差值,只能与 date类，datetime类进行加减运算
'''

import datetime
'''
1. data 类
'''
# 获取data对象
d = datetime.date(2022, 3, 27)
# print(d) # 2022-03-27

# 获取 date对象的个个属性
# print(d.year)
# print(d.month)
# print(d.day)

'''
2. time 类
'''
# 获取time对象
t = datetime.time(9,37,59)
# print(t) # 09:37:59

# 获取 time对象的各个属性
# print(t.hour)
# print(t.minute)
# print(t.second)

'''
3. datatime 类
主要用于数学计算.
'''
# 获取 datatime 对象
dt = datetime.datetime(2022,3,27,9,40,59)
# print(dt) # 2022-03-27 09:40:59

# datatime 类: 年月日时分秒，主要用于数学计算.

'''
4. timedelta 类: 就是时间的变化量
'''
td = datetime.timedelta(days=1)
# print(td)

'''参与数学运算:
只能 date 类， datetime类 与 timedelta 参数数学运算
'''
# 1.创建时间对象 date datetime timedelta
d = datetime.date(2022,3,1)
res = d + td
# print(res)

# 2.时间变化量的计算，是否会产生进位？ 会产生进位
# 1> 'datetime.time' and 'datetime.timedelta' datatime.time 不能与 datetime.timedelta 运算
# t = datetime.time(10,10,59)
# td = datetime.timedelta(seconds=3)
# res = t+td # TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.timedelta'
# print(res)

# 2> datatime.datetime 可与 datetime.timedelta 运算
t = datetime.datetime(2022,3,27,10,1,59)
td = datetime.timedelta(seconds=3)
res = t + td # 2022-03-27 10:02:02
# print(res)

'''
datetime 模块练习题：
'''
# 1. 计算某一年的二月份有多少天？
# 普通算法：根据年份计算是否是闰年？是 29天，不是28天
# 用 datetime模块计算：
# 1>首先创建出指定年份的3月1号，然后让它往前走一天
# year = int(input("输入年份:"))
# 2> 创建指定年份的date对象
# d = datetime.date(year,3,1)
# 3> 创建一天的时间段
# td = datetime.timedelta(days=1)
# res = d - td
# print(res, res.day, type(res))


'''
5. 和时间段进行运算的结果是什么时间类型？ 数据类型与运算符前面的数据类型相同
'''

d = datetime.date(2022, 3, 27)
td = datetime.timedelta(days=1)
res = d + td
print(res, type(res)) # 2022-03-28 <class 'datetime.date'>

d1 = datetime.datetime(2022,3,27,10,37,50)
res1 = d1 + td
print(res1,  type(res1)) # 2022-03-28 10:37:50 <class 'datetime.datetime'>

