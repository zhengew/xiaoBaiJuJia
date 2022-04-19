'''
# date 20220417
# time 192001
# datetime 20220417192001

# datetime
# year
# date
# time
# timestamp
'''

# create table t4(
#     dt datetime,
#     y year,
#     t time,
#     d date,
#     ts timestamp
# );


# mysql> create table t5(
#     -> id int,
#     -> dt datetime NOT NULL                        # 不能为空
#                   DEFAULT CURRENT_TIMESTAMP        # 默认是当前时间
#                   ON UPDATE CURRENT_TIMESTAMP);    # 在更新的时候使用当前时间更新字段