'''
1、查询男生、女生的人数；
mysql> select gender, count(1) as count from student group by gender;
+--------+-------+
| gender | count |
+--------+-------+
| 男     |    10 |
| 女     |     6 |
+--------+-------+
2 rows in set (0.01 sec)

2、查询姓“张”的学生名单；
mysql> select * from student t where t.sname like '张%';
+-----+--------+----------+--------+
| sid | gender | class_id | sname  |
+-----+--------+----------+--------+
|   3 | 男     |        1 | 张三   |
|   4 | 男     |        1 | 张一   |
|   5 | 女     |        1 | 张二   |
|   6 | 男     |        1 | 张四   |
+-----+--------+----------+--------+
4 rows in set (0.00 sec)

3、课程平均分从高到低显示
select s.course_id, c.cname, avg(num) as avg_score
     from score s inner join course c on s.course_id = c.cid
     group by s.course_id
     order by avg_score desc;
+-----------+--------+-----------+
| course_id | cname  | avg_score |
+-----------+--------+-----------+
|         4 | 美术   |   85.2500 |
|         2 | 物理   |   65.0909 |
|         3 | 体育   |   64.4167 |
|         1 | 生物   |   53.4167 |
+-----------+--------+-----------+
4 rows in set (0.00 sec)

4、查询有课程成绩小于60分的同学的学号、姓名；
select s.student_id, stu.sname/*, c.cname, s.num*/
    from score s
        inner join student stu on s.student_id = stu.sid
        left join course c on c.cid = s.course_id
    where s.num < 60;
+------------+--------+--------+-----+
| student_id | sname  | cname  | num |
+------------+--------+--------+-----+
|          1 | 理解   | 生物   |  10 |
|          1 | 理解   | 物理   |   9 |
|          2 | 钢蛋   | 生物   |   8 |
|          4 | 张一   | 物理   |  11 |
|          5 | 张二   | 物理   |  11 |
|          6 | 张四   | 生物   |   9 |
|          7 | 铁锤   | 生物   |   9 |
|          8 | 李三   | 生物   |   9 |
|          9 | 李一   | 美术   |  22 |
|         10 | 李二   | 体育   |  43 |
|         11 | 李四   | 体育   |  43 |
|         12 | 如花   | 体育   |  43 |
+------------+--------+--------+-----+
12 rows in set (0.00 sec)

5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
select s.course_id from score s where s.student_id = '1';

select distinct stu.sid, stu.sname
    from student stu
        inner join score s on s.student_id = stu.sid
        where s.course_id in (select s.course_id from score s where s.student_id = '1')
        and s.student_id != '1'
        order by stu.sname;
+-----+--------+
| sid | sname  |
+-----+--------+
|  12 | 如花   |
|   4 | 张一   |
|   3 | 张三   |
|   5 | 张二   |
|   6 | 张四   |
|   9 | 李一   |
|   8 | 李三   |
|  10 | 李二   |
|  11 | 李四   |
|   2 | 钢蛋   |
|   7 | 铁锤   |
+-----+--------+
11 rows in set (0.00 sec)

6、查询出只选修了一门课程的全部学生的学号和姓名；
select s.student_id, stu.sname
    from student stu
        inner join score s on s.student_id = stu.sid
        group by s.student_id
        having count(s.student_id) = 1
        order by stu.sid;
+------------+--------+
| student_id | sname  |
+------------+--------+
|         13 | 刘三   |
+------------+--------+
1 row in set (0.00 sec)

7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select s.course_id 课程ID, max(s.num) 最高分, min(s.num) 最低分
    from score s
    group by s.course_id;

+----------+-----------+-----------+
| 课程ID   | 最高分    | 最低分    |
+----------+-----------+-----------+
|        1 |        91 |         8 |
|        2 |       100 |         9 |
|        3 |        87 |        43 |
|        4 |       100 |        22 |
+----------+-----------+-----------+
4 rows in set (0.00 sec)

8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
select student_id, course_id, num from score where course_id = '2';
select student_id, course_id, num from score where course_id = '1';

# 拿到2张表，分别存储课程1，2的学生id 课程id, 成绩
select student_id, course_id, num as num1
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = '1') course1

select student_id, course_id, num as num2
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = '2') course2

# 找出课程2成绩比课程1成绩低的 student_id,在获取学生姓名
select c2.student_id, stu.sname -- , c2.num2, c1.num1
from
(select student_id, course_id, num as num1
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = '1') course1) c1 right join

(select student_id, course_id, num as num2
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = '2') course2) c2 on c1.student_id = c2.student_id
                        join student stu on c2.student_id = stu.sid
group by c2.student_id, c2.num2, c1.num1
having c2.num2 < c1.num1;

+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
8 rows in set (0.00 sec)


9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；

select c2.student_id -- , stu.sname , c2.num2, c1.num1
from
(select student_id, course_id, num as num1
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = (select cid from course where cname = '生物')) course1) c1 right join

(select student_id, course_id, num as num2
    from (
        select s.student_id, s.course_id, s.num, count(s.course_id) n
                        from score s
                        group by s.student_id, s.course_id, s.num
                        having n = 1 and s.course_id = (select cid from course where cname = '物理')) course2) c2 on c1.student_id = c2.student_id
                        join student stu on c2.student_id = stu.sid
group by c2.student_id, c2.num2, c1.num1
having c2.num2 < c1.num1;

+------------+--------+------+------+
| student_id | sname  | num2 | num1 |
+------------+--------+------+------+
|          1 | 理解   |    9 |   10 |
|          3 | 张三   |   66 |   77 |
|          4 | 张一   |   11 |   79 |
|          5 | 张二   |   11 |   79 |
|          9 | 李一   |   88 |   91 |
|         10 | 李二   |   77 |   90 |
|         11 | 李四   |   77 |   90 |
|         12 | 如花   |   77 |   90 |
+------------+--------+------+------+
8 rows in set (0.00 sec)

10、查询平均成绩大于60分的同学的学号和平均成绩;
select s.student_id, avg(num) as avg_score
    from score s inner join student stu on s.student_id = stu.sid
    group by s.student_id
    having avg_score > 60;
+------------+-----------+
| student_id | avg_score |
+------------+-----------+
|          3 |   82.2500 |
|          4 |   64.2500 |
|          5 |   64.2500 |
|          6 |   69.0000 |
|          7 |   66.0000 |
|          8 |   66.0000 |
|          9 |   67.0000 |
|         10 |   74.2500 |
|         11 |   74.2500 |
|         12 |   74.2500 |
|         13 |   87.0000 |
+------------+-----------+
11 rows in set (0.00 sec)

11、查询所有同学的学号、姓名、选课数、总成绩；
# 使用连接查询的时候，那张表的数据多，以那张表为准，避免丢失数据
select stu.sid, stu.sname, count(s.course_id), count(s.num)
    from score s right join student stu on s.student_id = stu.sid
    group by stu.sid;
+-----+--------+--------------------+--------------+
| sid | sname  | count(s.course_id) | count(s.num) |
+-----+--------+--------------------+--------------+
|   1 | 理解   |                  3 |            3 |
|   2 | 钢蛋   |                  3 |            3 |
|   3 | 张三   |                  4 |            4 |
|   4 | 张一   |                  4 |            4 |
|   5 | 张二   |                  4 |            4 |
|   6 | 张四   |                  4 |            4 |
|   7 | 铁锤   |                  4 |            4 |
|   8 | 李三   |                  4 |            4 |
|   9 | 李一   |                  4 |            4 |
|  10 | 李二   |                  4 |            4 |
|  11 | 李四   |                  4 |            4 |
|  12 | 如花   |                  4 |            4 |
|  13 | 刘三   |                  1 |            1 |
|  14 | 刘一   |                  0 |            0 |
|  15 | 刘二   |                  0 |            0 |
|  16 | 刘四   |                  0 |            0 |
+-----+--------+--------------------+--------------+
16 rows in set (0.00 sec)

12、查询姓“李”的老师的个数；
select count(1) from teacher t where t.tname like '李%';
+----------+
| count(1) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)

13、查询没学过“张磊老师”课的同学的学号、姓名；
select tid from teacher where tname = '张磊老师' -- tid = 1
# 张磊的课程id
select cid from course c where c.teacher_id = (select tid from teacher where tname = '张磊老师') -- cid = '1'

# 统计至少学习了张磊课程的学生id，然后再从student表去除学了张磊课程的sid
select sid, sname
    from student
    where sid not in(
        select distinct student_id
            from (select student_id
                    from score s
                    where course_id in( select cid from course c where c.teacher_id = (
                            select tid from teacher where tname = '张磊老师'))) stu);
+-----+--------+
| sid | sname  |
+-----+--------+
|  13 | 刘三   |
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四   |
+-----+--------+
4 rows in set (0.00 sec)

14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
# 先查询学过课程2的，再从学过课程1的里面取交集
select s.student_id, stu.sname
    from score s inner join student stu on s.student_id = stu.sid
    where s.course_id = '1' and s.student_id in (
        select student_id from
            (select s.student_id, count(course_id) num, s.course_id
                from score s
                group by student_id, course_id
                having course_id = '2' and num = 1) course1);

+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          6 | 张四   |
|          7 | 铁锤   |
|          8 | 李三   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
11 rows in set (0.00 sec)

15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
# 查询他交的课程
select cid from course where teacher_id = (select tid from teacher where tname = '李平老师') -- 2, 4

select s.student_id, stu.sname -- , s.course_id
    from score s inner join student stu on s.student_id = stu.sid
    where s.course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '李平老师'))
    group by s.student_id
    having count(s.student_id) = 2
    order by s.student_id;
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          6 | 张四   |
|          7 | 铁锤   |
|          8 | 李三   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
11 rows in set (0.01 sec)

1、查询没有学全所有课的同学的学号、姓名；
# 找出学全的，在从student表排除
select stu.sid, stu.sname
    from student stu
    where stu.sid not in(
        select student_id from (
            select s.student_id, count(1) as num
                from score s
                group by s.student_id
                having num = (select count(1) from course)) as sco);
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 理解   |
|   2 | 钢蛋   |
|  13 | 刘三   |
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四   |
+-----+--------+
6 rows in set (0.00 sec)

2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
select course_id from score where student_id = '002'
# 002 学了3门课程，
# 把002没学的,其他人学了的 同学去除
select distinct student_id
    from score where student_id not in(
        select student_id from score where course_id not in (
            select course_id from score where student_id = '002'))
# 然后比较 学的课程数量，如果都和002相同，证明是一样的
select count(course_id) from score where student_id = '002' -- 3

# 各种嵌套，太烦了
select res2.student_id, stu.sname
from
    (select student_id, count(1) as num
        from
            (select s.student_id, s.course_id
                from score s
                group by s.student_id, s.course_id
                having s.student_id in(
                        select distinct student_id
                            from score where student_id not in(
                                select student_id from score where course_id not in (
                                    select course_id from score where student_id = '002')) and student_id != '002'
                        )) res
                        group by res.student_id) res2 inner join student stu on res2.student_id = stu.sid
                        where res2.num = (select count(course_id) from score where student_id = '002');

+------------+--------+
| student_id | sname  |
+------------+--------+
|         13 | 刘三   |
+------------+--------+
1 row in set (0.00 sec)

3、删除学习“李平老师”老师课的SC表记录；
# 找tid
select tid from teacher where tname = '李平老师'
# 找 cid
select cid from course c where c.teacher_id = (select tid from teacher where tname = '李平老师');
# 删除 cid对应的记录
# delete from score s where s.course_id in(select cid from course c where c.teacher_id = (select tid from teacher where tname = '李平老师'))

# 备份数据
# create table score_back select * from score;
# select * from score_back;

4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 
# 没上过002课程的学号
select stu.sid from student stu where stu.sid not in (select student_id from score where course_id = '002')
+-----+
| sid |
+-----+
|   2 |
|  13 |
|  14 |
|  15 |
|  16 |
+-----+
5 rows in set (0.00 sec)
# 002 课程平均成绩
select avg(num) from score s where s.course_id = '002';
+----------+
| avg(num) |
+----------+
|  65.0909 |
+----------+
1 row in set (0.00 sec)
# 插入数据
insert into score values(null, 2, 2, 65.0909), (null, 13, 2, 65.0909), (null, 14, 2, 65.0909), (null, 15, 2, 65.0909), (null, 16, 2, 65.0909);

+------------+------+------+-----+---------+----------------+
| Field      | Type | Null | Key | Default | Extra          |
+------------+------+------+-----+---------+----------------+
| sid        | int  | NO   | PRI | NULL    | auto_increment |
| student_id | int  | NO   | MUL | NULL    |                |
| course_id  | int  | NO   | MUL | NULL    |                |
| num        | int  | NO   |     | NULL    |                |
+------------+------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

5、按平均成绩从低到高显示所有学生的“生物”、“物理”、“体育”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
select cid from course where cname = '生物'; -- 1
select cid from course where cname = '物理'; -- 2
select cid from course where cname = '体育'; -- 3

# 拿到每名学生的 生物物理体育成绩
select s.student_id, s.num as biology from score s where s.course_id = (select cid from course where cname = '生物')
select s.student_id, s.num as physics from score s where s.course_id = (select cid from course where cname = '物理')
select s.student_id, s.num as sports from score s where s.course_id = (select cid from course where cname = '体育')

# 取到学生的成绩和考试课程数，和平均分数
select stu.sid 学生ID, b.biology 生物, p.physics 物理, s.sports 体育, count(b.biology) + count(p.physics) + count(s.sports) 有效课程数, sum(ifnull(b.biology, 0) + ifnull(p.physics, 0) + ifnull(s.sports, 0)) / 3 有效平均分
    from student stu
    left join (select s.student_id, s.num as biology from score s where s.course_id = (select cid from course where cname = '生物')) as b on stu.sid = b.student_id
    left join (select s.student_id, s.num as physics from score s where s.course_id = (select cid from course where cname = '物理'))  as p on b.student_id = p.student_id
    left join (select s.student_id, s.num as sports from score s where s.course_id = (select cid from course where cname = '体育')) as s on s.student_id = p.student_id
    group by stu.sid , b.biology, p.physics, s.sports
    order by stu.sid;

+----------+--------+--------+--------+-----------------+-----------------+
| 学生ID   | 生物   | 物理   | 体育   | 有效课程数      | 有效平均分      |
+----------+--------+--------+--------+-----------------+-----------------+
|        1 |     10 |      9 |   NULL |               2 |          6.3333 |
|        2 |      8 |   NULL |   NULL |               1 |          2.6667 |
|        3 |     77 |     66 |     87 |               3 |         76.6667 |
|        4 |     79 |     11 |     67 |               3 |         52.3333 |
|        5 |     79 |     11 |     67 |               3 |         52.3333 |
|        6 |      9 |    100 |     67 |               3 |         58.6667 |
|        7 |      9 |    100 |     67 |               3 |         58.6667 |
|        8 |      9 |    100 |     67 |               3 |         58.6667 |
|        9 |     91 |     88 |     67 |               3 |         82.0000 |
|       10 |     90 |     77 |     43 |               3 |         70.0000 |
|       11 |     90 |     77 |     43 |               3 |         70.0000 |
|       12 |     90 |     77 |     43 |               3 |         70.0000 |
|       13 |      9 |   NULL |   NULL |               1 |          3.0000 |
|       14 |   NULL |   NULL |   NULL |               0 |          0.0000 |
|       15 |   NULL |   NULL |   NULL |               0 |          0.0000 |
|       16 |   NULL |   NULL |   NULL |               0 |          0.0000 |
+----------+--------+--------+--------+-----------------+-----------------+
16 rows in set (0.00 sec)

6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

select s.course_id 课程ID, max(s.num) 最高分, min(s.num) 最低分
    from score s
    group by s.course_id
+----------+-----------+-----------+
| 课程ID   | 最高分    | 最低分    |
+----------+-----------+-----------+
|        1 |        91 |         8 |
|        2 |       100 |         9 |
|        3 |        87 |        43 |
|        4 |       100 |        22 |
+----------+-----------+-----------+
4 rows in set (0.00 sec)

7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；


8、查询各科成绩前三名的记录:(不考虑成绩并列情况) 
9、查询每门课程被选修的学生数；
10、查询同名同姓学生名单，并统计同名人数；
11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
15、求选了课程的学生人数
16、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
17、查询各个课程及相应的选修人数；
18、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
19、查询每门课程成绩最好的前两名；
select * from
(select student_id, course_id, num
    from score
    where course_id = '1'
    order by num desc
    limit 2) s1
union
select * from
(select student_id, course_id, num
    from score
    where course_id = '2'
    order by num desc
    limit 2) s2
union
select * from
(select student_id, course_id, num
    from score
    where course_id = '3'
    order by num desc
    limit 2) s3
union
select * from
(select student_id, course_id, num
    from score
    where course_id = '4'
    order by num desc
    limit 2) s4;

+------------+-----------+-----+
| student_id | course_id | num |
+------------+-----------+-----+
|          9 |         1 |  91 |
|         10 |         1 |  90 |
|          6 |         2 | 100 |
|          7 |         2 | 100 |
|          3 |         3 |  87 |
|         13 |         3 |  87 |
|          4 |         4 | 100 |
|          5 |         4 | 100 |
+------------+-----------+-----+
8 rows in set (0.00 sec)

20、检索至少选修两门课程的学生学号；
21、查询全部学生都选修的课程的课程号和课程名；
22、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
23、查询两门以上不及格课程的同学的学号及其平均成绩；
24、检索“004”课程分数小于60，按分数降序排列的同学学号；
25、删除“002”同学的“001”课程的成绩；

更多练习
'''
