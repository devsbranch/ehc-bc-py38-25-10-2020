# Exception Handling

# try:
#     to do this
# except:
#     if it fails then do this in this block
# finally/else:
#     if the try block worked correctly then eventually do this in here

# version 1.0 the failing file
# my_file = open("fail_then_pass.txt", 'r')
# my_file.write('Content that will not be written anywhere \n because the file does not exist')
# my_file.close()

# version 1.1 the failing file that still does not exist
# handle error using the try-except-else

# try:
#     my_file = open("fail_then_pass.txt", "r")
#     my_file.write("Content that will not be written anywhere \n because the file does not exist")
# except:
#     print("I could not find the file you are trying to open.")
# else:
#     my_file.close()

# version 1.2 with more precision, the acceptable way
# try:
#     my_file = open("fail_then_pass.txt", "r")
#     my_file.write("Content that will not be written anywhere \n because the file does not exist")
# except FileNotFoundError as file_error:
#     print(f"I could not find the file you are trying to open. \nError occured: {file_error}")
# else:
#     my_file.close()

# version 1.3 the finally block
# try:
#     with open("fail_then_pass.txt", "r") as passing_file:
#         print(passing_file.read())
#         # failing_file.write("Content that will not \n be written anywhere \n because the file does not exist")
# finally:
#     print("I will always be executed upon success of the try block")

# version 1.4 the correct way
# try:
#     with open("fail_then_pass.txt", "r") as working_file:
#         content = working_file.read()
#         print(content)
#
# except:
#     print("I Failed to run properly, something went wrong")
#
# else:
#     print("I will always run no matter what happened previously.")

# Working with databases version 1.0

import sqlite3

# db_location = "/Users/amukoma/Desktop/my_folder/chinook.db"

# create a db connection
# conn = sqlite3.connect(db_location)
# get_all_employees = """SELECT firstname, lastname, title, email FROM employees;"""

# my_army_knife = conn.cursor()
# all_employees = my_army_knife.execute(get_all_employees)
# for employee in all_employees:
#     # first approach - complex - one liners
#     # print(employee[0], employee[1], employee[2], employee[3])
#     first_name = employee[0]
#     last_name = employee[1]
#     title = employee[2]
#     email = employee[3]

    # print(f"Full name: {first_name} {last_name} \nEmail address: {email} \nJob Title: {title} \n\n")
    #
# conn.commit()
# cleanups
# close the army knife and close the connection
# my_army_knife.close()
# conn.close()


# Working with databases version 1.1 more profession and pythonic.
# using defensive programming to with work dbs

# lets define our problem

"""
# OUR FINANCE FRIEND'S NAME: Bessy

Hi Alison I need a quick urgent favour from you.
Could you please download my database called `chinook.db` and in it you will find the tables listed here below
```
albums          employees       invoices        playlists     
artists         genres          media_types     tracks        
customers       invoice_items   playlist_track
```
From it I would like to add an extra table called student records and have attributes like 
```student first and last name, email address, student id, course name, course level```
and I would like to have a few sample records added to this table. 

the second thing i would like you to help me with is get for me all the 
employee records and the attributes in that table and then I would like to have 
a simple text file called `all_employees.txt` and If you can save all these employee 
records which you got from the database employee table into this text file you would have 
saved me big time my friend. 
Because I will be then able to just click and view without worrying about
the SQL language that i do not know that will be glory to me.

By the way please save an employee record on one line of this text file only.

# Alison has already done this one guys so just worry about the context above.
But first the quick thing i would request from you is could you quickly 
show me the employee firstname, lastname, job title and their email address?
>>> Alison - reply: Oh year sure let me prepare some script for your last request my friend and then
I will ask my python buddies to look into the rest of your request 
because they are awesome and they will surely get it done for you I can promise.
"""

"""
Hey guys this is my example algorithm I prepared to help our friend Bessy with her last request.

- download the chinook database
- locate the database download location/ where i placed it
- copy the pathname for the database
- store the database pathname in a variable of my choice
- prepared an SQL querry to get employee attributes that Betty was interested in
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
# define our solution thoughtprocess

db_location = "/Users/amukoma/Desktop/my_folder/chinook.db"
get_all_employees = """SELECT firstname, lastname, title, email FROM employees;"""

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
    connection.commit()

except sqlite3.Error as e:
    print(f"Something went wrong with db operation as below \n{e}")

else:
    executioner.close()
    connection.close()
