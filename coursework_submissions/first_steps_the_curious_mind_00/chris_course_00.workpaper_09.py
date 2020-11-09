# Answer the following questions
'''Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.'''
# Numbers: Numbers are numeric data types that are used to represent the quantity of anything in python.
# Strings: Strings are words that are used in Python to keep information. These are sometimes nouns that reprents things.
# Lists: A list is a collection  which is ordered and changeable.
# Tuples: A tuple is a data type which is odered and unchangeable.
# Dictionaries: A dictionary is a set of keys that stores values in python. Dictionaries are written in brackets.
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25.
x = 1.25 + (5 ** 2 * 8 / 2) - 1
print(x)

# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5) = 44
# What is the value of the expression 4 * 6 + 5 = 29
# What is the value of the expression 4 + 6 * 5 = 34
a = 4 * (6 + 5)
b = 4 * 6 + 5
c = 4 + 6 * 5
print(a, b, c)

# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>
# Answer is Float, because the answer will have a decimal point.
# What would you use to find a number’s square root, as well as its square?
# Square root : n**(0.5)
y = 81 ** (0.5)
print(y)

# Square : n**2
x = 9 ** 2
print(x)

""" Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below: """
s = 'hello'
print(s [1])

# Reverse the string 'hello' using slicing
s = 'hello'
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
s = 'hello'
print(s[- 1])

# Method 2:
s = 'hello'
print(s [4])

# Lists
# Build this list [0,0,0] two separate ways
# Method 1:
my_list = [0, 0, 0]
print(my_list)

# Method 2:

# Reassign 'hello' in this nested list to say 'goodbye' instead.
list3 = [1, 2, [3, 4, 'hello']]
list3[2].pop(2)
print(list3)

list3[2].append('goodbye')
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

# Dictionaries
# Using keys and indexing, grab the ‘hello’ from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1])

# This will be hard and annoying!
d = {'k1':[1, 2, {'k2':['this is tricky',{'though':[1, 2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['though'][2])

# Sets
# What is unique about a set?
""" Use a set to find unique values of a set below: """
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))

# Booleans
# What will be the resulting Boolean of the following pieces of code(answer first then check by typing it in!)
# Answer before running cell 2 > 3 = false
print(2 > 3)

# Answer before running cell 3 <= 2 = false
print(3 <= 2)

# Answer before running cell 3 == 2.0 = false
print(3 == 2.0)

# Answer before running cell 3.0 == 3 true
print(3.0 == 3)

# Answer before running cell 4 ** (0.5) != 2 = false
print(4 ** (0.5) != 2)

# Final Question: What if the Boolean output of the cell block below?
# two nested lists
l_one = [1,2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
# true or false
l_one[2][0] >= l_two[2]['k1']
print(l_one[2][0] >= l_two[2]['k1'])