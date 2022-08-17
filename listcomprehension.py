# List comprehension offers a shorter syntax to create a new list based on the values of an existing list. 

# Exmaple 1 : 

# fruits = ['apple','banana','avocado','cherry', 'angelfruit']

# newlist = [ x.upper() for x in fruits if x[0]=='a' in x]

# print(newlist)

# example 2 : Replace banana with orange

fruits2 = ['apple','banana','avocado','cherry', 'angelfruit']

newlist2 = [ x if x != "banana" else "orange" for x in fruits2 ]

print(newlist2)

# In list comprehension if you want to write both if and else condition write it before the for statement 
# AND
# If you want to write only if statement then write it after the for statement. 