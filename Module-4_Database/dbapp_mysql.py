import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=dbcon.cursor()

# Create Table
create_tbl="create table studinfo(id integer primary key auto_increment,name text,city text)"

try:
    cur.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
stnm=input("Enter Name:")
stct=input("Enter City")
insert_data=f"insert into studinfo(name,city) values('{stnm}','{stct}')"

"""insert_data="insert into studinfo(name,city) values('sanket','rajkot'),('mitesh','baroda'),('nirav','ahmedabad'),('hiren','navsari'),('ashok','jamnagar')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data="update studinfo set name='abhishek' where id=5"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""delete_data="delete from studinfo where name='hiren'"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(2)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        #print(i)
        print(i[1])
except Exception as e:
    print(e)