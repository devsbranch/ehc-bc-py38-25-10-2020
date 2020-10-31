# question on numbers
y = 10 * 10 / 1 + 2**2 - 3.75
print ( y )

# answers without a code
44
29
34
# checking the answer with a code
firstnumber = 4
secondnumber = 6
thirdnumber = 5
# first expression 
res = firstnumber * ( secondnumber + thirdnumber)
print ( res )
# second expression 
result = firstnumber * secondnumber + thirdnumber
print ( result )
  
# third expression
results = firstnumber + secondnumber * thirdnumber
print ( results )

# type of results
#its float becuase one of the numbers is a float and results will be float as 

# finding the square root
#number ** number
j = 10 ** 10
print ( j ) 
# square 
#number ** 0.5
p = 81 ** 0.5
print ( p )

#strings
s = ' hello '
# printing in e 
s[2]
print ( s[2] )

#printing in reverse
s[::-1]
print ( s[::-1] )

# methods of printing o
s[5]
print ( s[5] )

s[-2]
print ( s[-2 ])

# list
# bluid the list [0,0,0] two separate ways
# method one, append 
list2 = [0,0,0]
list2.append ('1,2,3')
print (list2)

# method 2, reverse
list2.reverse()
print ( list2)
# reassign
list3 = [1,2,[3,4,'hello']]
list3[2] = 'goodbye'
print (list3)
# sort
list4 = [5,3,4,6,1]
list4.sort()
print (list4)

# dictionaries
d = {'simple_key':'hello'}
m = d.get ('simple_key')
print (m)
k = d ['simple_key']
print (k)

d = {'k1':{'k2':'hello'}}
j = d ['k1']['k2']
print (j)

d = {'k1': [ {'nest_key':['this is deep',['hello']]}]}
p = d['k1'][0]['nest_key'][1][0]
print (p)

d = {'k1':[1,2,{'k2':['this is trick',{'tough':[1,2,['hello']]}]}]}
f = d ['k1'][2]['k2'][1]['tough'][2][0]
print (f)

# tupples
# sets do not allow redandancy
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
print (set(list5))