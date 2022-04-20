# /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day42

# 表和数据的备份
    # 备份数据在cmd命令行直接执行
    # mysqldump -uroot -p123456 -h172.16.238.4 homework > /home/zew/tem.sql

    # 恢复数据，在mysql中执行命令
    # 切换到一个要备份的数据库中
    # sourse /home/zew/tem.sql

# 备份库
    # 备份
    # mysqldump -uroot -p123456 --databases homework > /home/zew/tem2.sql
    # 恢复
    # source /home/zew/tem2.sql

