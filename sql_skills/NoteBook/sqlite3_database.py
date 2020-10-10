import os
import sys
sys.path.append('../../')
from pysql import SQLite


sql = SQLite(database='./database/t.db')

sql('''
-- 学生表
-- Student(s_id，s_name，s_birth，s_sex)
-- 学生编号,学生姓名, 出生年月, 学生性别
create table if not exists Student(
    s_id VARCHAR(20),
    s_name VARCHAR(20) NOT NULL DEFAULT '',
    s_birth VARCHAR(20) NOT NULL DEFAULT '',
    s_sex VARCHAR(10) NOT NULL DEFAULT '',
    primary key (s_id)
);
''')

sql('''
-- 课程表
-- Course(c_id,c_name,t_id) 
-- 课程编号, 课程名称, 教师编号
create table Course(
    c_id VARCHAR(20),
    c_name VARCHAR(20) NOT NULL DEFAULT '',
    t_id VARCHAR(20) NOT NULL,
    primary key (c_id)
);
''')

sql('''
-- 教师表
-- Teacher(t_id,t_name)
-- 教师编号,教师姓名
create table Teacher(
    t_id VARCHAR(20),
    t_name VARCHAR(20) NOT NULL DEFAULT '',
    primary key (t_id)
);
''')

sql('''
-- 成绩表
-- Score(s_id,c_id,s_s_score) 
-- 学生编号,课程编号,分数
CREATE TABLE Score(
    s_id VARCHAR(20),
    c_id VARCHAR(20),
    s_score INT(3),
    PRIMARY KEY(s_id, c_id)
);
''')

sql('''
-- 学生表数据
insert into Student values
('01' , '赵雷' , '1990-01-01' , '男'),
('02' , '钱电' , '1990-12-21' , '男'),
('03' , '孙风' , '1990-05-20' , '男'),
('04' , '李云' , '1990-08-06' , '男'),
('05' , '周梅' , '1991-12-01' , '女'),
('06' , '吴兰' , '1992-03-01' , '女'),
('07' , '郑竹' , '1989-07-01' , '女'),
('08' , '王菊' , '1990-01-20' , '女');
''')

sql('''
-- 课程表数据
insert into Course values('01' , '语文' , '02'),('02' , '数学' , '01'),('03' , '英语' , '03');
''')

sql('''
-- 教师表数据
insert into Teacher values('01' , '张三'),('02' , '李四'),('03' , '王五');
''')

sql('''
-- 成绩表数据
insert into Score values
('01' , '01' , 80),('01' , '02' , 90),('01' , '03' , 99),('02' , '01' , 70),
('02' , '02' , 60),('02' , '03' , 80),('03' , '01' , 80),('03' , '02' , 80),
('03' , '03' , 80),('04' , '01' , 50),('04' , '02' , 30),('04' , '03' , 20), 
('05' , '01' , 76),('05' , '02' , 87),('06' , '01' , 31),('06' , '03' , 34),
('07' , '02' , 89),('07' , '03' , 98);
''')
