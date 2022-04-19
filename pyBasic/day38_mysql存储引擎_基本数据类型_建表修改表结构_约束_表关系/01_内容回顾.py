'''
# 数据库：DB
    # 所有的数据存放的仓库
    # 每一个文件也是一个数据库
# 数据库管理系统 - 软件 DBMS
    # 关系型数据库: mysql oracle
    # 非关系型数据库: redis mongodb
# 数据库管理员 DBA
    # 管理数据库软件
# 数据库服务器: 一台跑着DBMS的机器
# 表：文件，一张存储了数据的表
# 数据/记录：表中的信息，一行就是一条记录

# 用户相关操作
    # 查看当前用户：select user();
    # 给当前用户设置密码: set password = password('123')
    # 创建用户: create user '用户名'@'主机的ip/主机域名' identified by '密码'；
    # 授权并创建用户：grand select on dbname.* to '用户名'@主机ip/主机域名';
# 基础库/表/数据操作
    # 库 - 文件夹
        # create database dbname; 建库
        # use dbname; 切换库
        # show databases; 查看所有库
    # 表 - 文件
        # show tables; 查看库下的所有表
        # 创建表 create table tbname (fieldname, 数据类型(长度), ...);
        # 删除表 drop table tbname;
        # 查看表结构 desc tbname;
            # describe tbname;
    # 数据记录 - 文件中的内容
        # 增 insert into tbname values(一行数据), (一行数据);
        # 删 delete from tbname where 条件;
        # 改 update tbname set field1 = value1, field2 = value2 where 条件;
        # 查 select field from tbname;

'''