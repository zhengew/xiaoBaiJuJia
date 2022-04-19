'''
# 所谓连表
    # 总是在连接的时候创建一张大表，里面存放的是两张表的笛卡尔积
    # 再根据条件筛选
    # mysql> select * from department d, employee e where d.id = e.dep_id;

# 表与表之间的连接方式：
    # 内连接 inner join ... on ...
        # select * form tb1 inner join tb2 on 条件
        # select * from department d inner join employee e on d.id = e.dep_id;
    # 外连接
        # 左外连接 left join ... on ...
            # select * from tb1 left join tb2 on 条件
            # select * from department d left join employee e on d.id = e.dep_id;
        # 右外连接 right join ... on ...
            # select * from tb1 right join tb2 on 条件
            # select * from department d right join employee e on d.id = e.dep_id;
        # 全外连接 full join
            # union 利用 union 合并 左外和右外连接
            # select * from department d left join employee e on d.id = e.dep_id
            # union
            # select * from department d right join employee e on d.id = e.dep_id;

# 练习：
# 1.找到技术部的所有人的姓名
select e.name, d.name
    from employee e inner join department d on e.dep_id = d.id
    where d.name = '技术';
# 2.找到人力资源部的年龄大于40岁的人的姓名
select e.name, e.age, d.name
    from employee e inner join department d on e.dep_id = d.id
    where d.name = '人力资源' and e.age > 40;

# 3.找到年龄大于25岁的员工以及员工所在的部门
select e.name, e.age, d.name from employee e inner join department d on e.dep_id = d.id where e.age > 25;

# 4.以内连接的方式查询employee和department表，并且age字段升序显示
select e.*, d.* from employee e inner join department d on e.dep_id = d.id order by e.age asc;

# 5.统计每个部门的人数
select d.id, d.name, count(e.id) from employee e right join department d on e.dep_id = d.id group by d.id, d.name;

# 5.统计每个部门的人数,且按照人数从高到低排序
select d.id, d.name, count(e.id) as c
    from employee e right join department d on e.dep_id = d.id
    group by d.id, d.name
    order by c desc;


# 所谓的连表，就是把两张表连接在一起之后，就变成一张大表，从from开始一直到on条件结束就看作一张表，
# 之后 where 条件，group by 分组 order by limit 都正常使用了

'''





