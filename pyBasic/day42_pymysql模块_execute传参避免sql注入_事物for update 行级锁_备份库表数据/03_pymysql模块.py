import pymysql
# 创建连接
# conn = pymysql.connect(user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
#         password='123456',
#         host='172.16.238.4',
#         database='homework',)

##  查询

# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 查询返回字典
# cur = conn.cursor()   # course 游标 # 默认返回元组
# try:
#     cur.execute('select * from students;')
#
#     ret = cur.fetchone()        # 获取一条结果
#     print(ret)
#     ret2 = cur.fetchmany(10)    # 获取多条结果
#     print(ret2)
#     ret3 = cur.fetchall()       # 获取全部结果
#     print(ret3)
# except pymysql.err.ProgrammingError as e: # 做异常处理时，控制台打印e,或者打到log里
#     print(e)
#
# conn.close() # 关闭连接
# cur.close()  # 关闭游标

## 增加，删除，修改
# conn = pymysql.connect(user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
#         password='123456',
#         host='172.16.238.4',
#         database='homework',)
#
# cur = conn.cursor()
# try:
#     # cur.execute("insert into student values(null, '男', 3, '大壮')")  # 增
#     # cur.execute("update student set gender = '女' where sid = 18")   # 删
#     # cur.execute("delete from student where sid in(20, 21)")          # 改
#     conn.commit() # 提交
# except Exception as e: # 异常处理要打印日志或者写log
#     print(e)
#     conn.rollback() # 如果出问题，回滚事物
#
# cur.close()
# conn.close()


## rowcount 获取查询结果的总行数
# rownumber 获取当前行

# conn = pymysql.connect(user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
#         password='123456',
#         host='172.16.238.4',
#         database='homework',)
#
#
# cur = conn.cursor()   # course 游标 # 默认返回元组
# try:
#     cur.execute('select * from student;')
#     print(cur.rowcount) # 获取查出使用多少行，便于使用fetchone取所有结果
#     for i in range(cur.rowcount):
#         ret = cur.fetchone()
#         print(cur.rownumber, ret)
# except pymysql.err.ProgrammingError as e: # 做异常处理时，控制台打印e,或者打到log里
#     print(e)
#
# conn.close() # 关闭连接
# cur.close()  # 关闭游标

## 实际操作mysql的时候会遇到一个问题

# 结合数据库和 python 写一个登陆
# usename password
# alex    3714

user = input('username:')
pwd = input('password:')
conn = pymysql.connect(user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
        password='123456',
        host='172.16.238.4',
        database='day42',)

cur = conn.cursor()
sql = "select * from userinfo where user = %s and password = %s"
cur.execute(sql, (user, pwd)) # sql用execute参数拼接，避免sql注入
print(cur.fetchone())

cur.close()
conn.close()

# sql 注入
