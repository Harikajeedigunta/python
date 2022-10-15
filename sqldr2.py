#pip install mysql-connector-python
#import mysql.connector
import sqlite3
mydb=sqlite3.connect(database="students")
mycur=mydb.cursor()
try:
    sql="""create table student_data(rollno,name,branch,college,phno,
    email)"""
    mycur.execute(sql)
except:
    pass
while True:
    ch=int(input("1.insert 2.display 3.exist"))
    if ch==1:
        d=tuple(map(str,input().split()))
        sel="select * from data where rollno like(?)"
        mycur.execute(sel,d[0])
        data=mycur.fetchall()
        if len(data)==0:
            ins="""
            insert into data(rollno,name,branch,college,phno,email)values(?,?,?,?,?,?)
            """
            mycur.execute(ins,d)
        else:
            print("data is already is the table")
        elif ch==2:
        sel="select * from data"
        mycur.execute("select * from data")
        data=mycur.fetchall()
        for d in data:
            print(*d)
     else:
        break
    mydb.commit()
        
breakmydb.commit(
            
            
    elif ch==2:
