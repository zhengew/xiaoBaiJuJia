# 数据准备
# 读取一次硬盘的时间开销
    # 磁盘的预读性原理
# 新的数据结构 -- 树
# mysql中存储数据的两种方式
    # 聚集索引
    # 非聚集索引
# 索引的创建与删除
    # 创建主键 primary key 聚集索引 + 非空 + 唯一
    # 创建唯一约束 unique  辅助索引 + 唯一
    # 添加一个普通索引
        # create index 索引名 on 表(字段);
        # drop index 索引名 on 表;
# 正确使用索引
    #

# 索引
    # 创建
    # 删除
    # 知道用了它会加快查询速度


'''
#方法一：创建表时
    　　CREATE TABLE 表名 (
                字段名1  数据类型 [完整性约束条件…],
                字段名2  数据类型 [完整性约束条件…],
                [UNIQUE | FULLTEXT | SPATIAL ]   INDEX | KEY
                [索引名]  (字段名[(长度)]  [ASC |DESC])
                );


#方法二：CREATE在已存在的表上创建索引
        CREATE  [UNIQUE | FULLTEXT | SPATIAL ]  INDEX  索引名
                     ON 表名 (字段名[(长度)]  [ASC |DESC]) ;


#方法三：ALTER TABLE在已存在的表上创建索引
        ALTER TABLE 表名 ADD  [UNIQUE | FULLTEXT | SPATIAL ] INDEX
                             索引名 (字段名[(长度)]  [ASC |DESC]) ;

#删除索引：DROP INDEX 索引名 ON 表名字;

'''