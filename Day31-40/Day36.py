# Day 36



import sqlite3

connection =sqlite3.connect('database.sqlite')
cursor = connection.cursor()

cursor.execute("""
create table stocks(
  id integer primary key,
  name text not null,
  buy integer not null,
  investor text not null
  )
""")


cursor.execute("""
insert into stocks(id,name,buy,investor)
values
(1,'ABC',29.45,'Nguyen'),
(2,'VIC',44.55,'Nguyen'),
(3,'GMD',74.30,'Nguyen'),
(4,'ACB',28.45,'Vinh'),
(5,'VIC',40.55,'Vinh'),
(6,'GMD',60.30,'Vinh')
""")
connection.commit()

# Câu 1: In tổng buy

import pandas as pd


data= pd.read_sql_query("select sum(buy) as sum_buy from stocks",connection)
print(f'Tổng giá bán là: {data.sum_buy}')

# Câu 2: tÌm giá mua cao nhất của từng nhà đầu tư



data= pd.read_sql_query("""

select  investor, name , max(buy) as max_price from stocks group by investor

  """,connection)
print(data)