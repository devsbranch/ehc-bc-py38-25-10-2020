"""
Hey guys this is my example algorithm I prepared to help our friend Bessy with her last request.
- download the chinook database
- locate the database download location/ where i placed it
- copy the pathname for the database
- store the database pathname in a variable of my choice
- prepared an SQL query to get employee attributes that Betty was interested in
- prepared the steps for the try except and else block 
- went into the try block
- store the db connection into a variable of my choice
- we request for the cursor object which then we can use to do things on the db 
- store the cursor (please name it whatever you like) object in a variable of your choosing
- run the executioner object on the db connection that I created
- I store the result into a variable of my choosing
 NOTE: REMEMBER: Betty was interested to see only a few details of the employee
- i go through or iterate through these employee records stored in the results i got back from the db cursor
 NOTE: what we get back is a tuple
- I save every employee detail in a variable of related name by using my skills of working with tuple 
- and then i simply print each employee set of records to the screen where Betty could see them as plain details
- and then knowing that bad things happen unexpectedly I went into my except block
- I stored the error provided by sqlite3 which is the db that am working with in my variable called `e`
- and then i constructed a useful error message for the user and then to the end I show the user the actual error stored in e
 NOTE: then knowing that if what i did in the try block would succeed, i then handle the following in the else block (which gets run ONLY if the try block worked.
- i give back the executioner knife to sqlite3 itself (close close)
- i also give back the database connection to sqlite3 (close things)
I think with this I can write version 1 of my code.
"""

import sqlite3
from tabulate import tabulate

# *************************************************************************************************************
"""
Task 1 - OUR FINANCE FRIEND'S NAME: Bessy
Hi Alison I need a quick urgent favour from you.
Could you please download my database called `chinook.db` and in it you will find the tables listed here below
```
albums          employees       invoices        playlists     
artists         genres          media_types     tracks        
customers       invoice_items   playlist_track
```
"""
try:
    db_location = "chinook.db"

    connection = sqlite3.connect(db_location)
    csr = connection.cursor()

    # -----List of Tables------
    db_tables = csr.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
    for i in db_tables:
        print('Table in chinook.db: ', i[0])

    # *************************************************************************************************************

    """Task - 2. The second thing i would like you to help me with is get for me all the
    employee records and the attributes in that table and then I would like to have
    a simple text file called `all_employees.txt` and If you can save all these employee
    records which you got from the database employee table into this text file you would have
    saved me big time my friend.
    Because I will be then able to just click and view without worrying about
    the SQL language that i do not know that will be glory to me.
    By the way please save an employee record on one line of this text file only.
    """
    all_employee_data = csr.execute("""SELECT * FROM employees""")
    # Employees data will return a collection af tuples, each containing all information of the employees.

    all_employees_info_lst = []
    # The the tuples returned by all_employee_data will be converted to a list and appended
    # to the all_employee_info_lst []. This will make it possible to print or write data
    # to file in a table using the tabulate function
    for employee in all_employee_data:
        all_employees_info_lst.append(list(employee))  # The tuple for each employee is appended to the employee_list.

    table = tabulate(all_employees_info_lst, headers=["employee ID", "Last Name", "First Name", "Title", "Reports to",
                                                      "Birth Date", "Hire Date", "Address", "City", "State", "Country",
                                                      "Postal code", "Phone", "Fax", "email"], tablefmt="fancy_grid")
    '''
    The tabulate() function from tabulate module will make it possible to print out or write the data to a file in a 
    Table populated with data. https://pypi.org/project/tabulate/
    It will iterate over every list of each employee in all_employees_info_lst and append the information to the table 
    each corresponding to it's row and column. 
    '''
    print('All Employees information', f'\n{table}')
    file = open('all_employees_data.txt', 'w')
    file.write(table)
    file.close()

    # **************************************************************************************************************
    """
    Task - 3. From it I would like to add an extra table called student records and have attributes like 
    ```student first and last name, email address, student id, course name, course level```
    """
    csr.execute("""DROP TABLE IF EXISTS students""")
    # If the students  table exists, the table will be dropped(deleted) and a new one will be created.

    csr.execute("""CREATE TABLE students
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL,
               email TEXT NOT NULL,
               course_name TEXT,
               course_level TEXT)
              """)  # Creates a Students Table

    # ************************************************************************************************************
    """
    Task - 4. # Alison has already done this one guys so just worry about the context above.
    But first the quick thing i would request from you is could you quickly
    show me the employee firstname, lastname, job title and their email address?
    #>>> Alison - reply: Oh year sure let me prepare some script for your last request my friend and then
    I will ask my python buddies to look into the rest of your request
    because they are awesome and they will surely get it done for you I can promise.
    """
    employee_data = csr.execute("""SELECT firstname, lastname, email FROM employees""")
    # Employee_data will return a collection af tuples, each containing the
    # firstname, lastname and email of the employees.

    employee_list = []
    # The the tuples returned by  employee_data will be converted o a list and appended to the employee_list [].
    # This will make it possible to print or write data to file in a table using the tabulate function

    for employee in employee_data:
        employee_list.append(list(employee))  # The tuple for each employee is appended to the employee_list.

    table2 = tabulate(employee_list, headers=["First name", "Last name", "email"], tablefmt="fancy_grid")
    '''
    The tabulate function from tabulate module will make it possible to print out or write the data to a file in a 
    Table populated with data. https://pypi.org/project/tabulate/
    It will iterate over every list of each employee in employee_lst and append the information to the table 
    each corresponding to it's row and column. 
    '''
    print('Bessy\'s request - Employee information', f'\n{table2}')
    file2 = open('employee_info.txt', 'w')
    file2.write(table2)
    file2.close()

    # **************************************************************************************************************
    """Task - 4. I would like to have a few sample records added to this table."""

    # Inserting data into the students table
    csr.execute("""INSERT INTO students
                 (first_name, last_name, email, course_name, course_level)
                 VALUES ('Nancy', 'Adams', 'nancy@chinookcorp.com', 'Short Course in Software Engineering', '3')""")
    csr.execute("""INSERT INTO students
                 (first_name, last_name, email, course_name, course_level)
                 VALUES ('Jachin', 'Manda', 'jmnda@chinookcorp.com', 'Short Course in Software Engineering', '1')""")

    # ********************************************************************************************************** 

    # ------ PRINTS OUT OR WRITE TO FILE STUDENT INFORMATION-----
    students_dt = csr.execute("""SELECT * FROM students""")

    std_lst = []
    for student in students_dt:
        std_lst.append(list(student))

    table3 = tabulate(std_lst, headers=["first_name", "last_name", "email", "course_name", "course_level"],
                      tablefmt="fancy_grid")
    print('Students information', f'\n{table3}')
    file3 = open('students.txt', 'w')
    file3.write(table3)

    connection.commit()
    csr.close()
    connection.close()

except sqlite3.OperationalError as e:  # Catches all Operational errors and prints them in the console
    print(f'''An error occurred: {e}. Possible cause could be incorrect file path, 
              unsupported file or extension, or Data being queried does not 
              exist in Database.''')
