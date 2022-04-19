'''
# 存储引擎 -- 存储数据的方式

# 1. 数据存储在硬盘上
#  一张表
    # 数据
    # 表的结构
    # 索引(查询的时候使用的一个目录结构)


# Innodb存储引擎（mysql5.6之后的默认存储引擎）
# 数据和索引存储在一起 2个文件
    # 数据索引/表结构
    # 数据持久化
    # 支持事物：为了保证数据的完整性，将多个操作变成原子性操作(原子性：不可拆分的)
    # 行级锁：修改的行少的时候使用                         -> 修改数据频繁的操作
    # 表级锁：批量修改多行的时候使用                       -> 对于大量数据的同时修改
    # 支持外键：约束两张表中的关联字段不能随意的添加、删除    -> 能够降低数据增删改的出错率

# Myisam存储引擎 mysql5.5之前的默认的存储引擎
# 数据和索引不存储在一起  3个文件
    # 数据/索引/表结构
    # 数据持久化
    # 支持表级锁

# Memory存储引擎
# 数据存储在内存中，也就是说数据断电消失 1个文件
    # 表结构
    # 数据断电消失

# 面试题
    # 你了解mysql的存储引擎么？
    # 你的项目用了什么存储引擎，为什么？
        # Innodb
        # 多个用户操作的过程中对同一张表的数据同时做修改
        # Innodb支持行级锁，所以我们使用了这个引擎
        # 为了适应程序未来的扩展性，扩展新功能的时候可能会用到...,涉及到要维护数据的完整性
        # 项目中有一两张xx表，之间的外间关系是什么，一张表的修改或者删除比较频繁，怕出错所以做了外键约束


补充：
    # select database() 查看当前库
    # show engines; # 查看当前版本支持的存储引擎
    # show variables like '%engine%'
    # creat table tbname(fdname type) engine = Innodb; 创建表，并指定存储引擎

mysql> show engines;
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
'''
