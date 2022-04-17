# int 不约束长度，最多表示10位数
# float(m,n)
    # m 一共多少位
    # n小数位多少位


# create table t1(
#     id int, # 默认是有符号的
#     age tinyint unsigned # 如果需要定义无符号的使用unsigned
# );

# create table t2(
#     f1 float(5,2), # 总共5位，整数位3，小数位2，保留两位小数并四舍五入
#     f2 float,
#     f3 double(5,2), # 同float
#     f4 double
# );

# create table t3(
#     d1 decimal(30, 20),
#     d2 decimal
# );