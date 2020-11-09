# Part 1 of the Question
# Algorithms
"""
- Download chinook.db
- locate the database downloaded and copy the pathname to the database
- create the database connection with a variable of own choice
- create a cursor to the connection
- create a table(students) using the sqlite.execute() method
- Also need to make sure that if the table is already existing in the database, prevent it from being dublicated
- by using 'DROP TABLE IF EXISTS'
- i also add the attributes(FirstName, LastName, EmailAddress, StudentID, CourseName, CourseLevel) to the table i have
  created using the sqlite.execute() methods
- i now insert the sample records in the fields created using the same method(sqlite.execute()method)
- from there i want to convince myself that the table i created is really existing in the database,
 so i perform the 'fetchall()' method to check if the records are entered.
 - for now, i can say goodbye to the first task Bessy asked me to do by committing the connection changes to the database,
  but i do not give a close to the connection because i still need to perform task 2.
"""
# Actual Python Code

import sqlite3
db_location = "/C:/Users/user/Desktop/Software Engineering/Python Practicals/chinook.db"
conn = sqlite3.connect(db_location)
my_file = conn.cursor()

with conn:
    my_file.execute("DROP TABLE IF EXISTS Students")
    my_file.execute("CREATE TABLE Students(FirstName TEXT, LastName TEXT, Email TEXT, StudentID INT, CourseName TEXT, CourseLevel INT)")
    my_file.execute("INSERT INTO students VALUES('Given', 'Moola', 'moolagiven@yahoo.com', 191920, 'Certificate in Software Engineering', 1)")
    my_file.execute("INSERT INTO students VALUES('Chris', 'Musiwa', 'chrismusiwa@gmail.com', 179014, 'Certificate in Software Engineering', 2)")
    my_file.execute("INSERT INTO students VALUES('Mwala', 'Zuze', 'mwalazuze@gmail.com', 172019, 'Diploma in Human Resourse Management', 3)")

my_file.execute("SELECT * FROM Students")
rows = my_file.fetchall()
for row in rows:
    print(row)
conn.commit()

# part 2 of the Question
# Algorithms

"""
- since sqlite3 has already being imported, database already located and database connection already being established, 
 i just go on get all the employee records and attributes as Bessy requested.
- I use the sqlite3.execute() method to select all the employees records from the employees table.
- from there i use the fetchall() method to find and get all the records,
 and then use the for loops and print to display all the records for employees.
- After that i create a text file called (all_employees.txt) to write and save all the employee records that will make 
 it easy for Bessy to read.
-This has proved to be a tricky task for me and i think Bessy will excuse me on this one as i still want to research to
 find the possible solution for this problem.
- I close the connection to the database 'conn.close()'
"""

# Actual Python Code

my_file.execute("""SELECT * FROM employees""")
rows = my_file.fetchall()
for row in rows:
    print(row)

