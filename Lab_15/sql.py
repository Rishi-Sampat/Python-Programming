import sqlite3
conn=sqlite3.connect('student_record.db')
cursor=conn.cursor()
print("Database connected successfully!")

cursor.execute("DROP TABLE IF EXISTS student_record")
#added this drop line as to exceute everytime it will nor show dupliacte error
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record( 
               Enrollment INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL, 
               Subject TEXT NOT NULL, 
               Mark INTEGER NOT NULL)''')


#CREATE TABLE-Creates a new table in the database
#IF NOT EXISTS-Prevents error if the table already exist
#PRIMARY KEY-Each row will have a unique value here (no duplicates).
#AUTOINCREMENT-Values are automatically assigned (1, 2, 3..)

conn.commit()#stors permanantly


student_record=[
    (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
    (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
    (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
]
cursor.executemany('''INSERT INTO student_record(Enrollment,name,subject,Mark)
                   VALUES(?,?,?,?)''',student_record)
conn.commit()

cursor.execute('SELECT*FROM student_record')
#*-fetch all rows
rows=cursor.fetchall()#will be list of tuples
#.cursor-as data will be stored in cursor pointer
#fetchall-all rows
print("All Student Records:")
for i in rows:
    print(i)

cursor.execute('SELECT name,subject,Mark FROM student_record WHERE Mark>90')
high_marks=cursor.fetchall()
print("\n Students with Marks greater than 90:")
for i in high_marks:
    print(i)

cursor.execute('''UPDATE student_record SET Mark=98
               WHERE name='ASHUTOSH KUMAR SINGH' AND subject='PWP' ''')
conn.commit()
cursor.execute('SELECT name,Mark FROM student_record WHERE name="ASHUTOSH KUMAR SINGH"')
update_mark=cursor.fetchone()
print(f"\nUpdate Mark for {update_mark[0]}:{update_mark[1]}")

cursor.execute('''DELETE FROM student_record WHERE name='DEVENDRASINH DOLATSINH JADEJA' ''')
conn.commit()
cursor.execute('SELECT*FROM student_record WHERE name="DEVENDRASINH DOLATSINH JADEJA"')
deleted_name=cursor.fetchone()
if(deleted_name is None):
    print("\n DEVENDRASINH DOLATSINH JADEJA has been succefully deleted.")

cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark=cursor.fetchone()[0]
print(f"\n The averge mark of student is:${avg_mark:.2f}")
conn.close()