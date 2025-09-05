import sqlite3
conn=sqlite3.connect('student_record.db')
cursor=conn.cursor()
print("Database connected successfully!")

cursor.execute("DROP TABLE IF EXISTS student_record")
cursor.execute("DROP TABLE IF EXISTS subjects")

cursor.execute('''CREATE TABLE IF NOT EXISTS student_record(
               Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL)''')
cursor.execute('''
               CREATE TABLE subjects(
               SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
               Enrollment INTEGER,
               Subject TEXT NOT NULL,
               Mark INTEGER NOT NULL,
               FOREIGN KEY (Enrollment) REFERENCES student_record(Enrollment)
               )''')

students = [
    ('ASHUTOSH KUMAR SINGH',),
    ('HARSH VISHALBHAI TRIVEDI',),
    ('VIRAJ PRAKASHBHAI VAGHASIYA',),
]
cursor.executemany('INSERT INTO student_record(name) VALUES(?)', students)

subjects = [
    (1, 'PWP', 95),
    (2, 'DBMS', 90),
    (3, 'PWP', 85),
    (4, 'OOP', 88),
    (5, 'PWP', 92),
    (6, 'Maths', 89)
]
cursor.executemany('INSERT INTO subjects( Enrollment,Subject, Mark) VALUES(?,?,?)', subjects)

cursor.execute('''
SELECT s.name, sub.Subject, sub.Mark
FROM student_record s
JOIN subjects sub ON s.Enrollment = sub.Enrollment
''')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()