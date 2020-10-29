# Numbers:
"""
Numbers are objects that hold value and can be classified as integers or float
"""
# Strings:
"""
A string is a sequence of aphabetic characters.
"""
# List: 
"""
A list is a collection of items which can be changed or ordered
"""
# Tuples:
"""
Tuples are a collection of oredered items which are immutable and are written inside round brackets
""""
# Dictionaries:
"""
A dictionary is a list written with curly brackets and is unordered, changeable and indexed
"""
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
20.05 * 5 # multiplication
501.25 / 5 # division
11 ** 2 - 20.75 # exponent
100 + 0.25 # addition
150.25 - 50 # subtraction
"""
 Answer these 3 questions without typing code. Then type code to check your answer.
"""
a = 4
b = 6
c = 5
# What is the value of the expression 4 * (6 + 5)
a * b + c = 44
# What is the value of the expression 4 * 6 + 5
a * b + c = 29
# What is the value of the expression 4 + 6 * 5 
a + b * c = 34
# What is the type of the result of the expression 3 + 1.5 + 4?
# The answer is 8.5 which is a float
# What would you use to find a number’s square root, as well as its square?
# You can use the exponent to find the square root, e.g
16 ** 0.5 = 4
# You can also use the exponent to find the square, e.g
4 ** 2 = 16
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1])
# Reverse the string 'hello' using slicing:
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[-1])
print(s[4])
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
# Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
 print(list4)
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])
# prints "hello"
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
# prints "hello"
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
# prints "hello"
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# Can you sort a dictionary? Why or why not?
# A dictionary cannot be sorted but you can get a representation of a dictionary sorted by item or by value

# What is the major difference between tuples and lists?
# A list is mutable while a tuple is immutable meaning a list can be changed while a tuple cannot be changed

# How do you create a tuple?
# A tuple is created by placing different elements of the same or different types insde round brackets separated by commas.

# What is unique about a set?
# The unique feature of a set is that it does not allow duplicates. Each element is unique

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
2 > 3 # false
3 <= 2 # false
3.0 == 3 # True
4**0.5 != 2 # false

# Final Question: What is the boolean output of the cell block below?
l_one[2][0] >= l_two[2]['k1']
# is false because l_one[2][0] = 3 and l_two[2]['k1'] = 4
# hence l_one[2][0] < l_two[2]['k1']
