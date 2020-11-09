#Answer the following questions
#Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.'''
#Numbers: Numbers are numeric data types that are used to represent the quantity of anything in python.
#Strings: Strings are words that are used in Python to keep information. These are sometimes nouns that reprents things.
#Lists: A list is a collection  which is ordered and changeable.
#Tuples: A tuple is a data type which is odered and unchangeable.
#Dictionaries: A dictionary is a set of keys that stores values in python. Dictionaries are written in brackets.
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25.
x = 1.25+(5**2*8/2)-1
print(x)

#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5) = 44
#What is the value of the expression 4 * 6 + 5 = 29
#What is the value of the expression 4 + 6 * 5 = 34
a = 4 * (6 + 5)
b = 4 * 6 + 5
c = 4 + 6 * 5
print(a,b,c)

#What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>
#Answer is Float, because the answer will have a decimal point.
#What would you use to find a number’s square root, as well as its square?
#Square root : n**(0.5)
y = 81**(0.5)
print(y)

#Square : n**2
x = 9**2
print(x)

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = hello
print(s[2])

#Reverse the string 'hello' using slicing
s = hello
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
#Method 1:
s = hello
print(s[-1])

#Method 2:
s = hello
print(s[4])
