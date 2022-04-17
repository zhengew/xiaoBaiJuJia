'''
# 约束某一个字段
# 无符号的 int unsigned
# 不能位空 not null
# 唯一约束 unique
    # 联合唯一约束 unique(field1, field2)
# 默认值是什么 default
# 自增
    # auto_increment
    # 只能对数字有效，自带非空约束
    # 至少是unique约束之后才能使用 auto_increment
    # 插入的时候给自增列传null,入库时自增列会自动增加
# 主键 primary key  非空+唯一
    # 一张表只能有一个
    # 如果不指定主键，默认是第一个非空+唯一约束的键
    # 联合主键 primary key(field1, field2)

# 外键 foreign key
    # foreign key(自己的字段) references 外表(外表的字段)
    # foreign key(class_id) references class(id) on update cascade on delete cascade
        # 外键级联更新(不安全) on update cascade
        # 外键级联删除(不安全) on delete cascade 尽量不用

'''

# create table t10(
#     id int unsigned
# );
#
# create table t11(
#     id int unsigned not null,
#     name char(18) not null
# );

# 并别单选，默认值为 male
# create table t12(
#     id int unsigned not null,
#     name char(18) not null,
#     male enum('male','female') not null default 'male'
# );


# 唯一约束 unique  值不能重复,但是Null可以写入多个
# create table t13(
#     id1 int unique,
#     id2 int
# );

# # 联合唯一 unique
# # ERROR 1062 (23000): Duplicate entry '192.168.1.100-9001' for key 't14.ip'
# create table t14(
#     id int,
#     servername char(12),
#     ip char(15),
#     port char(5),
#     unique(ip, port)
# );

# 非空+唯一约束
    # 第一个被定义为非空+唯一的那一列会成为这张表的主键 primary key
    # 一张表只能定义一个主键
# create table t15(
#     id int not null unique,
#     username char(18) not null unique
# );
# mysql> desc t15;
# +----------+----------+------+-----+---------+-------+
# | Field    | Type     | Null | Key | Default | Extra |
# +----------+----------+------+-----+---------+-------+
# | id       | int      | NO   | PRI | NULL    |       |
# | username | char(18) | NO   | UNI | NULL    |       |
# +----------+----------+------+-----+---------+-------+
# 2 rows in set (0.00 sec)

# create table t17(
#     username char(18) not null unique,
#     id int primary key
# );

## 联合主键 primary key(field1, field2)
# create table t18(
#     id int,
#     servername char(12),
#     ip char(15),
#     port char(5),
#     primary key(ip, port)
# );

# mysql> desc t18;
# +------------+----------+------+-----+---------+-------+
# | Field      | Type     | Null | Key | Default | Extra |
# +------------+----------+------+-----+---------+-------+
# | id         | int      | YES  |     | NULL    |       |
# | servername | char(12) | YES  |     | NULL    |       |
# | ip         | char(15) | NO   | PRI | NULL    |       |
# | port       | char(5)  | NO   | PRI | NULL    |       |
# +------------+----------+------+-----+---------+-------+
# 4 rows in set (0.00 sec)

# 自增
# create table t20(
#     id int primary key auto_increment,
#     name char (12)
# );
# insert into t20 (name) values('eva');
# insert into t20 value (null, 'zew'); # 自增列传null值

# 外键
# 学生表
# create table stu(
#     id int primary key auto_increment,
#     name char(12) not null,
#     gender enum('male', 'female') default 'male',
#     class_id int,
#     foreign key(class_id) references class(id)
# );
# 班级表
# create table class(
#     id int primary key auto_increment,
#     cname char(12) not null,
#     startd date
# );
#
# # 外键级联更新(不安全) on update cascade
# # 外键级联删除(不安全) on delete cascade 尽量不用
# create table stu(
#     id int primary key auto_increment,
#     name char(12) not null,
#     gender enum('male', 'female') default 'male',
#     class_id int,
#     foreign key(class_id) references class(id) on update cascade on delete cascade
# );


