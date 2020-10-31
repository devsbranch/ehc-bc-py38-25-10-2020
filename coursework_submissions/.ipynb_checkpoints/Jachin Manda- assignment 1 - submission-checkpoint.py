# Objects and Data Structures Assessment Test

'''Write (or just say out loud to yourself) a brief description of all the following
 Object Types and Data Structures we've learned about'''

# Numbers: Numbers are refered to as intergers and can be used to perform mathematical operation. There are two types int(whole number) and float(int with decimal point)

# Strings: Strings are literally a piece of text with quotation marks which can thought of as a sentence.

# Lists: Lists are ordered sequence of characters. They are mutable. It's contents are called items and can be of any type e.g numbers, strings, booleans. The are inclosed in square brackets.

# Tuples: Tuples are like list but are immutable and it's items are enclosed with () brakets.

# Dictionaries: A dictionary is unordered, changeable and indexed. It's both a data type and a data structure(meaning a collection that holds data which can be manipulated and used in the code)

#-------------------------------------------------------------------------------------------------------------------


# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

multiplication = 50.125 * 2 # ANSWER = 100.25
division = 1000.25 / 10 # Answer = 100.25
addition = 49 + 11 + 40.25 # Answer = 100.25
subtraction = 295 - 120 - 30.125 - 44.625# Answer = 100.25


# What is the value of the expression 4 * (6 + 5)?
  4 * (6 + 5)  #Answer = 44 because expression in brackets will be evaluated first then multiplied by 4

# What is the value of the expression 4 * 6 + 5?
  4 * 6 + 5  # Answer = 29 because of multiplication first then addition.


# What is the value of the expression 4 + 6 * 5?
  4 + 6 * 5  # Answer = 34 because multiplication first then addition


# What is the type of the result of the expression 3 + 1.5 + 4?
answer = float

 
# What would you use to find a number’s square root, as well as its square?
squareroot = number ** (1/2) 
# OR
squareroot_2 = math.sqrt(number)

square = number ** 2

#--------------------------------------------------------------------------------------------------------------------

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1]) # will print 'e'

#Reverse the string 'hello' using slicing:
print(s[::-1])



#Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'
​# Method 1:
	print(s[4])
​# Method 2:
​	print(s[-1])
​

# Lists
# Build this list [0,0,0] two separate ways.

# Method 1:
print(s[4:])
​
# Method 2:
print(s[-1:])
​

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
​
​
#Sort the list below:

list4 = [5,3,4,6,1]
list4.sort()
​
​
# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

print(d['simple_key']) # Grabs 'hello'
​
d2 = {'k1':{'k2':'hello'}}
print(d['k1']['k2']) # Grabs 'hello'
​

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key']['hello']) #Grabs hello
​
​
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['hello'][2]['k2'][1]['tough'][2]) #Grabs hello

# Can you sort a dictionary? Why or why not?
# It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted.


# Tuples
# What is the major difference between tuples and lists?
# tuples are immutable/not changeable while lists are mutable


# How do you create a tuple?
tuple1 = (1,2,5,8,10)


# Sets
# What is unique about a set? 
# Items in sets are ordered and there are no duplicates


# Use a set to find the unique values of the list below.
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5)) #This will convert the list to a set and the set will remove duplicates. So the output will be unique items in list.

​
#Booleans
# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

'''Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) 

<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b)

<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)'''

# Answer before running cell
2 > 3  true

# Answer before running cell
3 <= 2 false

# Answer before running cell
3 == 2.0 false

# Answer before running cell
3.0 == 3 True
# Answer before running cell
4**0.5 != 2 

#Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
​
# True or False?
l_one[2][0] >= l_two[2]['k1'] = FALSE
