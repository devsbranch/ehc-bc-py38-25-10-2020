"""
-download the database and rename it sa kukash
-store the database path in a variable called db_location
-add a table called student_records with the following fields:
student's first name
student's last name
student's email address
student's ID
course name
course level
"""
import sqlite3
db_location = "C:/Users/Rhema/PycharmProjects/pythonProject1/kukash.db"
con = sqlite3.connect('db_location')  # create connection to database
myfile = con.cursor()

with con:
    myfile.execute("CREATE TABLE student_records(FName TEXT, LName TEXT, email TEXT, SID INT, course_name TEXT, course_level INT)")
    # create table
    myfile.execute("INSERT INTO student_records VALUES('chola', 'mwansa', 'cm@ehc.zm', 2260, 'EEE', 1)")
    myfile.execute("INSERT INTO student_records VALUES('dan', 'hope', 'dan@ehc.zm', 3131, 'DIT', 1)")
    # insert student records
    
# display student records
    myfile.execute("SELECT * FROM student_records")
    rows = myfile.fetchall()
    for row in rows:
        print(row)
    con.commit()

 # display employees details

db_location = "C:/Users/Rhema/PycharmProjects/pythonProject1/kukash.db"
get_all_employees = 'SELECT * FROM employees'
import sqlite3

try:
    connection = sqlite3.connect(db_location)
    executioner = connection.cursor()
    all_employees = executioner.execute(get_all_employees)
    for employee in all_employees:
        first_name = employee[0]
        last_name = employee[1]
        title = employee[2]
        email = employee[3]
        print(f"Full name: {first_name} {last_name} \nEmail address: {email} \nJob Title: {title} \n")

except sqlite3.Error as e:
    print(f"Something went wrong with the database operation \n{e}")

else:
    executioner.close()
    connection.close()


