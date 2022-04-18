'''
create table t1(
	id INT PRIMARY KEY auto_increment,
	username char(12) not null,
	sex enum('male', 'female') DEFAULT('male'),
	hoby set('上课', '写作业', '考试')
);

-- 增 insert into 表(字段...) values (值...)
insert into t1 values(1, '大壮', 'male', '上课,写作业');
insert into t1 values(2, 'alex', 'male', '写作业,考试');
insert into t1 values(3, 'b哥', 'male', '写作业,考试'),(4, '庄博', 'male', '考试');

insert into t1 (username, hoby) values('杨得港', '上课,写作业,考试'),('李帅','考试');
select * from t1;

insert into t2 (id,name) select id,username from t1; -- 复制其他表的数据

-- 删
create table t2(
	id int,
	name char(12)
);

insert into t2 (id,name) select id,username from t1;
select * from t2;

-- 删除表
-- 清空表
-- delete from tbname;
	-- 会清空表，但是是不会清空自增字段的offset(偏移量)值
	-- truncate table tbname;
	-- 会清空表和自增字段的偏移量
--删除某一条数据必须跟where条件
	-- delete from tbname where 条件
	-- 正常都是先查询结果，判断是否查询准确，再删除，避免操作失误
delete from t1 where id = 3;
select * from t1;
delete from t1; -- 清空 t1
show create table t1;

-- 改
	-- update tbname set field = value where 条件
	-- update tbname set field1 = value, field2 = value where 条件; -- 修改多个列
select * from t1;
update t1 set hoby = '上课', id = 1 where username = '李帅';

# 10个查询对应1个增删改


'''