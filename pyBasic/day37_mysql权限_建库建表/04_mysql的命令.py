# 环境变量
# python -->python.exe
# 在任何目录下都能够找到python.exe文件
# 才能在任意位置输入python命令启动python解释器

## win用法
# mysqld install 安装mysql服务 mysql服务就被注册到操作系统中
# net start mysql 启动mysql服务（开机自启动）

## 启动客户端连接server
# mysql -uroot -p123 -h192.168.14.12 # 连接其他人的客户端
# select user(); 查看当前登陆用户
# 创建一个其他用户
#

## 账号相关
'''
#进入mysql客户端
$mysql
mysql> select user();  #查看当前用户
mysql> exit     # 也可以用\q quit退出

# 默认用户登陆之后并没有实际操作的权限
# 需要使用管理员root用户登陆
$ mysql -uroot -p   # mysql5.6默认是没有密码的
#遇到password直接按回车键
mysql> set password = password('root'); # 给当前数据库设置密码

# 创建账号
mysql> create user 'eva'@'192.168.10.%'   IDENTIFIED BY '123';# 指示网段
mysql> create user 'eva'@'192.168.10.5'   # 指示某机器可以连接
mysql> create user 'eva'@'%'                    #指示所有机器都可以连接
mysql> show grants for 'eva'@'192.168.10.5';查看某个用户的权限
# 远程登陆
$ mysql -uroot -p123 -h 192.168.10.3

# 给账号授权
grant 权限类型 on dbname.* for 'user'@'ip'
grant all on *.* to 'eva'@'%';
grant select
grant select, insert
flush privileges;    # 刷新使授权立即生效

grant select on day37.* to 'guest'@'172.16.238.4';
# 创建账号并授权 mysql 8.0 不支持
mysql> grant all on *.* to 'eva'@'%' identified by '123'

# 创建数据库@
create database day37;

# 操作数据库
# show databases; 查看所有库
# create database dbname; 创建库
# use dbname; 切换到这个库
# show tables; 查看库下的所有表
# drop database dbname; 删除库

# 操作表
# 创建一张表
create table tablename(
    name char(12),
    age int
);
# 查看表结果
desc student;

##  操作数据
# 插入数据 inset into tbname values('alex', 18);
# 查询数据 select * from student;
# 修改数据 update tbname set fieldname = values where 条件;
# 删除数据 delete from tbname where 条件;
#
'''





''' linux
# 启停服务
systemctl {start|stop|restart|status} mysqld.service
systemctl start mysqld.service

# 查看服务状态
systemctl status mysqld.service

# 安全初始化
/usr/bin/mysql_secure_installation

# 停系统防火墙
systemctl stop firewalld.service

# 查看强制访问控制状态
getenforce

# 关闭强制访问控制策略
setenforce 0

# 创建root远程登陆密码
mysql -h 127.0.0.1 -u root -p

mysql> grant all privileges on *.* to root@'%' identified by "root";

mysql> flush privileges;

'''