"""
map (function just name,  iterables can be many separated by comma )
but there should be corresponding numbers of parameters in function to handle it. 

e.g. 
def myfunc(a,b):
    return a + b

x = map(func, l1,l2)

"""

# numbers = ["4","6","23"]

# for i in numbers:

#     print(int(i)+1)

#================ Calculates the squares of numbers ====================

# numbers = ["4","6","3","8"]
# squares = list(map(lambda a: int(a)**2,numbers))
# print(squares)

"""
map(function, list)

"""
#=======================================================================

# List can also store functions. 

# def squares(a):
#     return a**2

# def cube(a):
#     return a**3

# func = [squares(5),cube(9)]
# print(func)

# t1 = ("hello","world")

# map_res = tuple(map(lambda x : x.upper(), t1))
# map_res = tuple(list(lambda x : x.upper(), t1))

# print (map_res)

#=============== Convert the map into list or tuple for readibility. 