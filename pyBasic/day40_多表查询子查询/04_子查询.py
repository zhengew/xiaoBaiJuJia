''' 子查询
# 查询平均年龄在25岁以上的部门名
    # 拆分需求
select d.name from department d where d.id in (
    select dep_id from employee group by dep_id having avg(age) > 25);

# 查看技术部员工姓名
select e.name from employee e where e.dep_id = (select id from department where name = '技术');

# 查看不足1人的部门名(子查询得到的是有人的部门id)
select d.name from department d where d.id not in (select distinct dep_id from employee e);

# 查询大于所有人平均年龄的员工名与年龄
select avg(age) from employee;
select e.name, e.age from employee e where e.age > (select avg(age) from employee);

# 查询大于部门内平均年龄的员工名、年龄
select e.name, e.age
    from employee e inner join
        (select e.dep_id as did, avg(age) as avg_age
            from employee e
            group by e.dep_id) as avg on e.dep_id = avg.did
    where e.age > avg.avg_age;


# exists关键字(有的地方还是需要的，不常用)
    # exists关键字返回bool值True/False
    # 返回True时，外层语句执行，返回False时，外层语句不执行

    mysql> select * from class where exists (select cid where caption = '一年二班');
    +-----+--------------+
    | cid | caption      |
    +-----+--------------+
    |   3 | 一年二班     |
    +-----+--------------+
    1 row in set (0.00 sec)

    mysql> select * from class where exists (select cid where caption = '一年一班');
    Empty set (0.00 sec)

'''