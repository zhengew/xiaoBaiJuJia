'''
create table 表名(
    id int,
    name char(18),
    字段名3 类型[(宽度), 约束条件]
);

# 放在中括号里的内容是可以不写的
'''

# 写入数据的方式：三种
# insert intto tbname values(值1,值2, ...);
    # 这张表有多少个字段就需要按照字段的顺序写入多少个值
# insert into tbname values(值1,值2, ...),(值1,值2, ...);
    # 一次性写入多行
# insert into tbname (字段1, 字段2) values(值1, 值2);
    # 指定字段名写入，可以任意的选择表中你需要写入的字典

# 查询表中的数据
    # select * from tbname;

# 查看表结构
    # desc tbname;
        # 能够查看有多少个字段、类型、长度，看不到表的编码、引擎，具体约束信息只能看到一部分；
    # show create table tbname \G; 查看表结构的全部属性