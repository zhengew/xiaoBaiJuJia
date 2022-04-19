# 数据库使用的时候有什么注意事项
    # 从搭建数据库的角度上来描述问题
    # 建表的角度上
        # 1.合理安排表关系
        # 2.尽量把固定长度的字段放在前面
        # 3.尽量使用char代替varchar
        # 4.分表: 水平分,垂直分
    # 使用sql语句的时候
        # 1.尽量用where来约束数据范围到一个比较小的程度,比如说分页的时候
        # 2.尽量使用连表查询而不是子查询
        # 3.删除数据或者修改数据的时候尽量要用主键作为条件
        # 4.合理的创建和使用索引
            # 1.查询的条件字段不是索引字段
                # 对哪一个字段创建了索引,就用这个字段做条件查询
            # 2.在创建索引的时候应该对区分度比较大的列进行创建
                # 1/10以下的重复率比较适合创建索引
            # 3.范围
                # 范围越大越慢
                # 范围越小越快
                # like 'a%'  快
                # like '%a'  慢
            # 4.条件列参与计算/使用函数
            # 5.and和or
                # id name
                # select * from s1 where id = 1800000 and name = 'eva';
                # select count(*) from s1 where id = 1800000 or name = 'eva';
                # 多个条件的组合,如果使用and连接
                    # 其中一列含有索引,都可以加快查找速度
                # 如果使用or连接
                    # 必须所有的列都含有索引,才能加快查找速度
            # 6.联合索引 : 最左前缀原则(必须带着最左边的列做条件,从出现范围开始整条索引失效)
                # (id,name,email)
                # select * from s1 where id = 1800000 and name = 'eva' and email = 'eva1800000@oldboy';
                # select * from s1 where id = 1800000 and name = 'eva';
                # select * from s1 where id = 1800000 and email = 'eva1800000@oldboy';
                # select * from s1 where id = 1800000;
                # select * from s1 where name = 'eva' and email = 'eva1800000@oldboy';
                # (email,id,name)
                # select * from s1 where id >10000 and email = 'eva1800000@oldboy';
            # 7.条件中写出来的数据类型必须和定义的数据类型一致
                # select * from biao where name = 666   # 不一致
            # 8.select的字段应该包含order by的字段
                # select name,age from 表 order by age;  # 比较好
                # select name from 表 order by age;  # 比较差





# select * from 表 where 条件 group by 分组 having 聚合;
# 300万条数据
# 分页
# page = 1
# num_per = 10
# tmp = (page-1)*num_per = 1-1=0*10 = 0
# select * from 表 where id between tmp and tmp+num_per
# page +=1 = 2
# tmp = (page-1)*num_per = 10
# select * from 表 where id between 10 and 20
#
# select * from 表 limit 10,10
# select * from 表 limit 20,10
#
# select * from 表 limit 2999990,10




















