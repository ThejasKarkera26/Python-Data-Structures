"""10. Create a table student table (regno, name and marks in 3 subjects) 
using MySQL/ SQLite and perform 
the followings 
a. To accept the details of students and store it in database. 
b. To display the details of all the students""" 
 
import sqlite3 
 
# Connect to SQLite database (creates database if it does not exist) 
conn = sqlite3.connect("student.db") 
 
# Create cursor object 
cur = conn.cursor() 
 
# Create student table 
cur.execute(""" 
CREATE TABLE IF NOT EXISTS student( 
    regno INTEGER PRIMARY KEY, 
    name TEXT, 
    sub1 INTEGER, 
    sub2 INTEGER, 
    sub3 INTEGER 
) 
""") 
 
# Accept student details 
n=int(input("Enter number of students:")) 
for i in range(n): 
    regno = int(input("Enter Register Number: ")) 
    name = input("Enter Student Name: ") 
    sub1 = int(input("Enter marks in Subject 1: ")) 
    sub2 = int(input("Enter marks in Subject 2: ")) 
    sub3 = int(input("Enter marks in Subject 3: ")) 
 
    # Insert values into table 
    cur.execute("INSERT INTO student VALUES(?,?,?,?,?)",(regno,name,sub1,sub2,sub3)) 
 
    # Save changes 
    conn.commit() 
 
    print("\nStudent record inserted successfully") 
 
# Display all student records 
print("\nStudent Details") 
print("RegNo\tName\tSub1\tSub2\tSub3") 
cur.execute("SELECT * FROM student") 
rows = cur.fetchall() 
for r in rows: 
    print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t",r[4]) 
# Close connection 
conn.close()

