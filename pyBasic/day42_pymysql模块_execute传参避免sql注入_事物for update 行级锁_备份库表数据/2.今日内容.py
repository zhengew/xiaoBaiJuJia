# pymysql
    # python操作mysql数据库
        # 连接数据库
        # 获取游标
        # 执行sql(增删改查)
        # 如果涉及到修改 : 提交
        # 关闭游标
        # 关闭库
    # sql注入
        # 传参数,注意sql注入的问题,传参数通过execute方法来传
        # execute('select * from 表 where name = %s',('alex',))
# mysql的库/表备份
# 事务
    # 锁

## 多线程或并发情况下，添加锁
# begin;  # 开启事务
# select * from emp where id = 1 for update;  # 查询id值，for update添加行锁；
# update emp set salary=10000 where id = 1; # 完成更新
# commit; # 提交事务










