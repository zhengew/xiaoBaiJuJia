# # 单表查询 https://www.cnblogs.com/Eva-J/articles/9688313.html
'''
# 1. select 语句

# 最简单的select
    # select * from 表;
    # select 字段... from 表;

# 重命名字段
    # select 字段 as 别名 from 表;
    # select 字段1 别名1, 字段2 别名2 from 表;

# distinct 去重
    # select distinct depart_id from employee;
    # 联合去重
        # select distinct age, sex from employee;

# 四则运算
    # mysql> select emp_name, salary * 12 as year_salary from employee; -- 求年薪 并起别名

select concat(emp_name, ':', salary*12) as info from employee;

# 使用函数
    # concat
    # concat_ws
# 使用判断逻辑
    # case when end 相当于if判断语句

# 练习：day39.employee
# 1 查出所有员工的名字，薪资,格式为
#     <名字:egon>    <薪资:3000>
# select concat('<名字:', emp_name, '>') as name, concat('<薪资:', salary, '>') as salary from employee;
# 2 查出所有的岗位（去掉重复）
# select distinct post from employee;
# 3 查出所有员工名字，以及他们的年薪,年薪的字段名为annual_year
# select emp_name, salary*12 as annual_year from employee;


# where 查询所有符合条件的行
    # 比较运算符
        # > < >= <= != <>
    # 范围
        # between  100 and 200
        # in
    # 模糊匹配
        # like
            # %  以什么开头，以什么结尾，包含什么的
            # 占位符号 _  一个字符长度的任意内容
        # regexp
            # '^a' 以什么开头
            # 'a$' 以什么结尾
            # 没啥用
    # 逻辑运算
        # not
        # and
        # or

# 分组 group by 根据谁分组，可以求这个组的总人数，最大值，最小值，平均值，求和，但是这个求出来的值，只是和分组字段对应
    # 并不和其他任何字段对应，这个时候查出来的所有其他字段都不生效
# 聚合函数
    # count 统计个数
    # max 最大值
    # min 最小值
    # avg 平均值
mysql> select * from employee where salary = (select min(salary) from employee); -- 工资最低的人


# having 分组之后的过滤
    # 在having条件中可以使用聚合函数，在where中不行
    # 适合去筛选符合条件的某一组的数据，而不是某一行
    # 先分组再过滤：求平均薪资大于xxx的部门，求人数大于xx的性别，求大于xx人的年龄段

# order by 排序
    # asc 默认升序
    # desc 降序
    # order by age, salary desc
        # 优先根据age升序，在age相同的情况下，更具薪资降序排列

# limit m,n
    # 从m+1项开始，取n项
    # 如果不写m，m默认为0

    # limit n offset m
        # 从第m+1项开始，取n项

mysql> select * from employee limit 3;
+----+----------+------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
| id | emp_name | sex  | age | hire_date  | post                                    | post_comment | salary     | office | depart_id |
+----+----------+------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
|  1 | egon     | male |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使              | NULL         |    7300.33 |    401 |         1 |
|  2 | alex     | male |  78 | 2015-03-02 | teacher                                 | NULL         | 1000000.31 |    401 |         1 |
|  3 | wupeiqi  | male |  81 | 2013-03-05 | teacher                                 | NULL         |    8300.00 |    401 |         1 |
+----+----------+------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
3 rows in set (0.00 sec)

mysql> select * from employtee limit 2,1;
ERROR 1146 (42S02): Table 'day39.employtee' doesn't exist
mysql> select * from employee limit 2, 1;
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
| id | emp_name | sex  | age | hire_date  | post    | post_comment | salary  | office | depart_id |
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
|  3 | wupeiqi  | male |  81 | 2013-03-05 | teacher | NULL         | 8300.00 |    401 |         1 |
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
1 row in set (0.00 sec)

mysql> select * from employee limit 1 offset 2;
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
| id | emp_name | sex  | age | hire_date  | post    | post_comment | salary  | office | depart_id |
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
|  3 | wupeiqi  | male |  81 | 2013-03-05 | teacher | NULL         | 8300.00 |    401 |         1 |
+----+----------+------+-----+------------+---------+--------------+---------+--------+-----------+
1 row in set (0.00 sec)
'''

''' having
1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select post, group_concat(emp_name), count(*) from employee group by post having count(*) < 2;
3. 查询各岗位平均薪资大于10000的岗位名、平均工资
4. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资

'''


''' 分组聚合
mysql> select * from employee where id = 11;
+----+----------+--------+-----+------------+------+--------------+---------+--------+-----------+
| id | emp_name | sex    | age | hire_date  | post | post_comment | salary  | office | depart_id |
+----+----------+--------+-----+------------+------+--------------+---------+--------+-----------+
| 11 | 丁丁     | female |  18 | 2011-03-12 | sale | NULL         | 1000.37 |    402 |         2 |
+----+----------+--------+-----+------------+------+--------------+---------+--------+-----------+
. 查询岗位名以及岗位包含的所有员工名字
select post, group_concat(emp_name) from employee group by post;
. 查询岗位名以及各岗位内包含的员工个数
select post, count(*) from employee group by post;
. 查询公司内男员工和女员工的个数
select sex, count(1) from employee group by sex;
. 查询岗位名以及各岗位的平均薪资
select post, avg(salary) from employee group by post;
. 查询岗位名以及各岗位的最高薪资
select post, max(salary) from employee group by post;
. 查询岗位名以及各岗位的最低薪资
select post, min(salary) from employee group by post;
. 查询男员工与男员工的平均薪资，女员工与女员工的平均薪资
select sex, avg(salary) from employee group by sex;
'''


''' employee
mysql> desc employee;
+--------------+-----------------------+------+-----+---------+----------------+
| Field        | Type                  | Null | Key | Default | Extra          |
+--------------+-----------------------+------+-----+---------+----------------+
| id           | int                   | NO   | PRI | NULL    | auto_increment |
| emp_name     | varchar(20)           | NO   |     | NULL    |                |
| sex          | enum('male','female') | NO   |     | male    |                |
| age          | int unsigned          | NO   |     | 28      |                |
| hire_date    | date                  | NO   |     | NULL    |                |
| post         | varchar(50)           | YES  |     | NULL    |                |
| post_comment | varchar(100)          | YES  |     | NULL    |                |
| salary       | double(15,2)          | YES  |     | NULL    |                |
| office       | int                   | YES  |     | NULL    |                |
| depart_id    | int                   | YES  |     | NULL    |                |
+--------------+-----------------------+------+-----+---------+----------------+
. 查看岗位是teacher的员工姓名、年龄
select emp_name, age from employee where post = 'teacher';
. 查看岗位是teacher且年龄大于30岁的员工姓名、年龄
select emp_name, age from employee where post = 'teacher' and age > 30;
. 查看岗位是teacher且薪资在9000-10000范围内的员工姓名、年龄、薪资
select emp_name, age, salary from employee where post = 'teacher' and salary between 9000 and 10000;
. 查看岗位描述不为NULL的员工信息
select * from employee where post_comment is not null;
. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
select emp_name, age, salary from employee where post = 'teacher' and salary in(10000, 9000, 30000);
. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
select emp_name, age, salary from employee where post = 'teacher' and salary not in (10000, 9000, 30000);
. 查看岗位是teacher且名字是jin开头的员工姓名、年薪
select emp_name, salary*12 as year_salary from employee where post = 'teacher' and emp_name like 'jin%';

'''
