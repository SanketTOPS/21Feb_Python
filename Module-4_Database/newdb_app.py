import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
"""create_tbl="create table sstudent(id int primary key auto_increment,name varchar(20), sub varchar(20), address text)"
try:
    dbcon._execute_query(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)"""

# Insert Data
"""insert_data="insert into student(name,sub,address) values('sanket','python','rajkot'),('mitesh','java','ahmedabad'),('nirav','php','surat'),('ashok','angular','morbi'),('hitesh','html','surat')"
try:
    dbcon._execute_query(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update student set address='jamnagar' where id=2"
try:
    dbcon._execute_query(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from student where id=2"
try:
    dbcon._execute_query(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show data
cr=dbcon.cursor()
show_data="select * from student"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchwarnings()
    print(data)
    for i in data:
        print(i[3])
except Exception as e:
    print(e)