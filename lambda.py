def myfunc(n):
    return lambda x:x*n

mydoubler = myfunc(2)

mytripler = myfunc(3)

print(mydoubler(20))

print(mytripler(20))