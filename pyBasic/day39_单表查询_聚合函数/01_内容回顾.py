# 存储引擎
    # Innodb mysql5.6之后的默认存储引擎
        # 2个文件,4个支持(支持事务,行级锁,表级锁,外键)
    # Myisam mysql5.5之前的默认存储引擎
        # 3个文件 支持表级锁
    # Memory
        # 1个文件 数据断电消失
# 数据类型
    # 数字 : bool int float(7,2)
    # 日期 : date time datetime year
    # 字符串 :
        # char    定长 效率高浪费空间 255
        # varchar 变长 效率低节省空间 65535
    # enum 和 set :
        # 单选和多选
# 约束
    # unsigned 无符号的
    # not null 非空
    # default  设置默认值
    # unique   唯一,不能重复
        # unique(字段1,字段2,字段3) 联合唯一
     # auto_increment 自增
        # int 必须至少unique字段,自带not null
    # primary key 主键
        # not null + unique
        # 一张表只能有一个主键
    # foreign key 外键
        # a表中有一个字段关联b表中的一个unique
        # a表中的是外键
# 建表
    # create table 表名(
    #   字段名1 类型(长度) 约束,
    #   字段名1 类型(选项) 约束,
    # );
# 修改表结构
    # alter table 表名 rename 新名字;
    # alter table 表名 add 字段名 类型(长度) 约束 after 某字段;
    # alter table 表名 drop 字段名;
    # alter table 表名 modify 字段名 类型(长度) 约束 first;
    # alter table 表名 change 旧字名 新名字 类型(长度) 约束;
# 表之间的关系
    # 一对一
    # 一对多
    # 多对多