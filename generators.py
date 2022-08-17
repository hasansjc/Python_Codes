
l1 = [10,20,30,40,50]
#========================================================  

# Defining my generator function 
def mygenerator(list):                  # this accepts an argument , below is given an example which  -                                         works without argument
    for i in list:
        yield i  
        
#========================================================  
        
# Getting  values of mygenerator through for loop  
#------------------------------------------------    
# for i in mygenerator(l1):
#     print(i)

#========================================================  

# res = mygenerator(l1)

# print(res.__next__())
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

# Both the __next__() and next (res ) works perfectly fine 

#========================================================  
# Defining my generator function 
# def mygen2():                         # Works without any arguments.
#     yield 1
#     yield 2
#     yield 3

# res2 = mygen2()

# print(next(res2))
# print(next(res2))
# print(next(res2))

# for i in mygen2():
#     print(i)
    
#========================================================  

# Defining my generator function usign comprehension syntax.
#-----------------------------------------------------------

# We use () paranthesis and write list comprehension type of statement inside. 

# mygen3 = (x**3 for x in range(5))

# print (next(mygen3))
# print("coming after this")
# for x in mygen3:
#     print(x)