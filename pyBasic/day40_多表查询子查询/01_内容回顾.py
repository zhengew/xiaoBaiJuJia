# 数据的
# 增
    # insert into 表 values (值)
    # insert into 表(字段,字段2) values (值,值2)
    # insert into 表(字段,字段2) select 字段1,字段2  from 表2
# 删
    # delete from 表 where 条件;
    # truncate table 表名;
# 改
    # update 表 set 字段=值 where 条件;
# 查
    # select 字段 from 表
        # where 条件  根据条件筛选符合条件的行
        # group by 分组
        # having 过滤条件 根据分组之后的内容进行组的过滤
        # order by 排序
        # limit m,n 取从m+1开始的前n条

    # 1.where条件中不能用select字段的重命名
    # 2.order by 或者having可以使用select字段的重命名
        # 主要是因为order by 在select语句之后才执行
        # having经过了mysql的特殊处理,使得它能够感知到select语句中的重命名

    # 拓展
        # 在执行select语句的时候,实际上是通过where,group by,having这几个语句锁定对应的行
        # 然后循环每一行执行select语句