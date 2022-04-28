

drop TABLE if EXISTS student;

create table student(
`sno` int(5) not null,
`sname` varchar(3),
`ssex` varchar(1),`sbirthday` datetime not null,
`class` VARCHAR(10)
);
insert into student(`sno`,`sname`,`ssex`,`sbirthday`,`class`)
values
("108","曾华","男","1990/9/1","20033"),
("107","匡明","男","1989/8/9","20031"),
("101","王丽","女","1992/8/9","20033"),
("109","李军","男","1991/7/8","20033"),
("103","王芳","女","1993/7/9","20031"),
("105","陆君","男","1990/7/8","20031");




drop table if EXISTS course;
create table  course(
`cno`  VARCHAR(11) not null,
`cname` varchar(255) not null,
`tno` int(11)not null,
primary key (`cno`)
);
insert into course
(`cno`,`cname`,`tno`)
VALUES
("3-105","计算机导论","825"),
("3-245","操作系统","804"),
("6-166","数字电路","856"),
("9-888","高等数学","831");


DROP TABLE if EXISTS score;

create table score(
`sno` VARCHAR(10) not null,
`cno` varchar(20) not null,
`degree` varchar(15) not NULL
);

INSERT INTO `score`
(`Sno`, `Cno`,`Degree`)
values
("103","3-245","86"),
("105","3-245","75"),
("109","3-245","68"),
("103","3-105","92"),
("105","3-105","88"),
("109","3-105","76"),
("101","3-105","64"),
("107","3-105","91"),
("108","3-105","78"),
("101","6-166","85"),
("107","6-166","79"),
("108","6-166","81");



DROP TABLE if EXISTS teacher;
create table teacher
(`tno` VARCHAR(11) not null,
`tname` varchar(50) not null,
`tsex` varchar(1) null,
`tbirthday` datetime(6) not null,
`prof` varchar(50) not null ,
`depart` varchar(50) not null)
;

insert into `teacher`
(`tno`,`tname`,`tsex`,`tbirthday`,`prof`,`depart`)
values
('804','李成','男','1958/12/1','副教授','计算机系'),
('856','张翔','男','1969/3/12','讲师','电子工程系'),
('825','汪萍','女','1972/5/5','助教','计算机系'),
('831','柳冰','女','1977/8/14','助教','电子工程系');
commit;