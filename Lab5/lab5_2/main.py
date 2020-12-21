import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE students
 #                   (id integer not null ,first_name text, last_name text, birthday date,
  #                  faculty text,group_num integer, average_score float, grant integer,primary key(id))""")

# students = [('1','Stu','Dent','7/24/2000','FMI','422','3.6','1200'),
#             ('2','Dan','Dum','5/14/2000','FMI','412','4.6','2200'),
#             ('3','Stu','Last','6/27/2000','FMI','421','3.2','1000'),
#             ('4','Vlad','Len','3/04/2000','FMI','401','4.3','1900')]
#
# cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?,?,?,?)", students)
# conn.commit()

for row in cursor.execute("SELECT * FROM students ORDER BY average_score"):
    print(row)

sql = "SELECT COUNT(id) FROM students"
cursor.execute(sql)
print(cursor.fetchone())