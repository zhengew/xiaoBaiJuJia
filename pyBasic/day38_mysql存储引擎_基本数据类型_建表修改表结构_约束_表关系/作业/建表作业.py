# https://www.cnblogs.com/Eva-J/articles/9677452.html

'''
show tables;

create table class(
	cid INT PRIMARY KEY auto_increment,
	caption char(6) NOT NULL
);

create table student(
	sid int PRIMARY key auto_increment,
	sname char(18) NOT NULL,
	dender enum('male','female') NOT NULL DEFAULT('male'),
	class_id int NOT NULL,
	FOREIGN KEY(class_id) REFERENCES class(cid)
);

create table teacher(
	tid int PRIMARY key auto_increment,
	tname char(18) NOT NULL
);

create table course(
	cid int PRIMARY KEY auto_increment,
	cname char(18) NOT NULL,
	tearch_id int NOT NULL,
	FOREIGN KEY(tearch_id) REFERENCES teacher(tid)
);

create table score(
	sid int PRIMARY key auto_increment,
	student_id int NOT NULL,
	course_id int NOT NULL,
	number float(4,1) DEFAULT(0.0),
	CONSTRAINT student_sid_fk FOREIGN KEY(student_id) REFERENCES student(sid),
	CONSTRAINT course_cid_fk FOREIGN KEY(course_id) REFERENCES course(cid)
);
commit;

show tables;


'''