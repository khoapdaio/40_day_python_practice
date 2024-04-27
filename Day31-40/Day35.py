# Day 35

# B1: Tạo kết nối đến CSDL

import sqlite3

connection =sqlite3.connect('database.sqlite')
cursor = connection.cursor()

# B2: Tạo bảng

cursor.execute("""
create table products(
  id integer primary key,
  name text not null,
  price integer not null
  )
""")

# B3: insert data

cursor.execute("""
insert into products(id,name,price)
values
(1,'iPhone 15',18000000),
(2,'Galaxy Z-Fold 5',30000000)
""")


# B4: show data

import pandas as pd


data= pd.read_sql_query("select * from products",connection)
print(data)

# B5: update data

cursor.execute("""

update products
set price =50000000
where id =2
""")
data= pd.read_sql_query("select * from products",connection)
print(data)

# B6: delete data


cursor.execute("""

delete from products
where id = 1
""")
data= pd.read_sql_query("select * from products",connection)
connection.commit()
print(data)