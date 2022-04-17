'''
enum 单选
set 多选 # 插入值时会去重，并且如果不再默认值里面的不会插入表

'''

# create table t8(
#     id int,
#     name char(18),
#     gender enum('male', 'fmale')
# );
#
# create table t9(
#     id int,
#     name char(18),
#     hoby set('抽烟', '喝酒', '汤头', '洗脚')
# );
#
# insert into t9 values(1, 'tbjx', '抽烟,喝酒,汤头'); # set类型字段插入值的时候，值与值之间不能有空格