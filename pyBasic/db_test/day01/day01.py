'''
1.统计 student学生表中 1990年-2000年出生的人数。
select count(1) as num from student s where date_format(sbirthday, '%Y') between 1990 and 2000;
select count(1) as num from student s where s.sbirthday between '1990-01-01' and '2000-12-31'
2.查询 学生姓名，性别，年龄，班级。
select sname, ssex, round(datediff(sysdate(), sbirthday)/365,2) as age, class from student;

3.每门课都及格的同学 姓名 ,班级。
# 先找出不及格的学生id
select sno from score where degree < 60;

select distinct stu.sname, stu.class
 from student stu inner join score s on s.sno = stu.sno
 where stu.sno not in(select distinct sno from score where degree < 60);


4.每个班级的同学人数。
select class, count(*) as num from student group by class;

5. 统计每个学生的考试成绩总分，没有考试成绩的话 总分为0，  输出 学号，姓名，总分；
主要考察两个知识点：
  a. left join 以学生表为主，统计所有学生表的数据。没有与之对应的数据则显示为Null
  b. ifnull 函数，如果为空则显示 为0.

select stu.sno, stu.sname, ifnull(num, 0) as num
    from student stu
    left join ( select sno, sum(ifnull(degree, 0)) as num from score group by sno)as s
    on stu.sno = s.sno
    order by stu.sno;

+-----+--------+-----+
| sno | sname  | num |
+-----+--------+-----+
| 101 | 王丽   | 149 |
| 103 | 王芳   | 178 |
| 105 | 陆君   | 163 |
| 107 | 匡明   | 170 |
| 108 | 曾华   | 159 |
| 109 | 李军   | 144 |
| 110 | 张三   |   0 |
+-----+--------+-----+
7 rows in set (0.00 sec)

6.统计每个班的平均分,输出班级，平均分；
select cno, round(avg(degree),2) as avgScore from score group by cno order by cno;
+-------+----------+
| cno   | avgScore |
+-------+----------+
| 3-105 |     81.5 |
| 3-245 |    76.33 |
| 6-166 |    81.67 |
+-------+----------+
3 rows in set (0.00 sec)

7.每个老师对应有多少个同学。 输出老师名字，对应学生数量。
# 每门课程有几个学生选修
select cno, count(*) as num from score group by cno;
# 课程与老师的对应关系
select c.cno, c.tno, t.tname from course c inner join teacher t on c.tno = t.tno;
# 最终结果
select t.tname , ifnull(s.num, 0) as num
 from course c
 inner join teacher t on c.tno = t.tno
 left join (select cno, count(*) as num from score group by cno) s on c.cno = s.cno

+--------+-----+
| tname  | num |
+--------+-----+
| 李成   |   3 |
| 张翔   |   3 |
| 汪萍   |   6 |
| 柳冰   |   0 |
+--------+-----+
4 rows in set (0.00 sec)


8.输出老师名字，教授的课程名字。
select t.tname, c.cname
 from teacher t left join course c on t.tno = c.tno;

+--------+-----------------+
| tname  | cname           |
+--------+-----------------+
| 李成   | 操作系统        |
| 张翔   | 数字电路        |
| 汪萍   | 计算机导论      |
| 柳冰   | 高等数学        |
+--------+-----------------+
4 rows in set (0.00 sec)
'''

''' db_test 表结构
mysql> show tables;
+-------------------+
| Tables_in_db_test |
+-------------------+
| course            |
| score             |
| student           |
| teacher           |
+-------------------+
4 rows in set (0.00 sec)

mysql> desc course;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| cno   | varchar(11)  | NO   | PRI | NULL    |       |
| cname | varchar(255) | NO   |     | NULL    |       |
| tno   | int          | NO   |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> desc score;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| sno    | varchar(10) | NO   |     | NULL    |       |
| cno    | varchar(20) | NO   |     | NULL    |       |
| degree | varchar(15) | NO   |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> desc student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| sno       | int         | NO   |     | NULL    |       |
| sname     | varchar(3)  | YES  |     | NULL    |       |
| ssex      | varchar(1)  | YES  |     | NULL    |       |
| sbirthday | datetime    | NO   |     | NULL    |       |
| class     | varchar(10) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> desc teacher;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| tno       | varchar(11) | NO   |     | NULL    |       |
| tname     | varchar(50) | NO   |     | NULL    |       |
| tsex      | varchar(1)  | YES  |     | NULL    |       |
| tbirthday | datetime(6) | NO   |     | NULL    |       |
| prof      | varchar(50) | NO   |     | NULL    |       |
| depart    | varchar(50) | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
'''