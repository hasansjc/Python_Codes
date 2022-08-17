from functools import reduce

l1 = [1,2,3,4,5,6,7,8,9,10]

# Using normal outside function.
#=====================================
# def add_two_num(a,b):
#     return a+b

# summation = reduce(add_two_num, l1)

# print(summation)
                 
                 
# Using lambda
#=====================================

summation = reduce(lambda x,y : x+y, l1)

print ("and the sum of the number is ",summation)