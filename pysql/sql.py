import pandas as pd
import sqlite3 #, psycopg2 https://www.cnblogs.com/lsdb/p/9835894.html
from sqlalchemy import create_engine # from sqlalchemy.types import Integer # import pandas.io.sql as psql


class SQLite:
    def __init__(self, database="./mydb.db"):

        # self.cx = sqlite3.connect("./{}".format(database))
        # self.cu = self.cx.cursor()
        self.engine = create_engine('sqlite:///{}'.format(database)) 
    
    def __call__(self, sql_code):
        self.engine.execute(sql_code)

    def execute(self, sql_code):
        return self.engine.execute(sql_code)
        # return self.cu.execute(sql_code) #.fetchall() self.cx.commit()

    def read_sql(self, sql_code):
        return pd.read_sql(sql_code, self.engine)


class SQL:
    def __init__(self, user="root", password="xierry", host='localhost', port="3306", database="mydb",):
        
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    
    def read_sql(self, sql_code):
        return pd.read_sql(sql_code, self.engine)
    
    def execute(self, sql_code):
        return self.engine.execute(sql_code)

# sql = SQL(user='root', port = '3306')

''' https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
            df.to_sql('df',engine,if_exists='replace append', index= False)
            engine.execute("SELECT * FROM users")
            order_info_utf = pd.read_csv('order_info_utf.csv', names = ['orderId', 'userId', 'isPaid', 'price', 'paidTime'] , header=None)
            order_info_utf.to_sql('order_info_utf', sql.engine, if_exists='append', index=False)
            user_info_utf = pd.read_csv('user_info_utf.csv', names = ['userId', 'sex', 'birth'] , header=None)
'''

'''
drop table if exists user_info;
'''

'''
insert into table_name values
    ('0003', null, null), 
    ('0004', null, null);
'''

'''
create table user_info(
    userid varchar(20) primary key not null,
    gender varchar(5) default null,
    birthday datetime default null 
);
'''

'''
create table order_info(
    orderid varchar(20) primary key not null,
    userid varchar(20) not null,
    ispaid varchar(20) default null,
    price float default null,
    paytime datetime default null
);
'''


'''
select count(t1.mon) as '3月购买', 
       count(t2.mon) as '4月回购', 
       count(t2.mon) / cast(count(t1.mon) as real) as '回购率'
from (
    select userid, strftime('%Y-%m', paytime) as mon from order_info
    where strftime('%m', paytime) = '03' and ispaid = '已支付'
    group by userid
) as t1
left join (
    select userid, strftime('%Y-%m', paytime) as mon from order_info
    where strftime('%m', paytime) = '04' and ispaid = '已支付'
    group by userid
) as t2
on t1.userid=t2.userid;
'''

'''
select 
    count(n1) as '三月购买人数', 
    count(
        case when n1 > 1 then 1 else null end
    ) as '三月复购人数', 
    count(
        case when n1 > 1 then 1 else null end
    )/cast(count(n1) as real) as '复购率'
from (
    select userid, count(1) as n1
    from order_info
    where strftime('%m', paytime) = '03' and ispaid='已支付'
    group by userid
) as t;
'''

'''
select gender as '性别', avg(cnt_per_user) as '平均采购次数' from (
    select o.userid, count(o.userid) as cnt_per_user, gender
    from order_info as o 
    join user_info as u
    on o.userid = u.userid
    where ispaid = '已支付' and gender <> ''
    group by o.userid
) as t
group by gender;
'''