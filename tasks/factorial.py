
from math import factorial


def myfactorial (num):
    
    # if(num==1):
        
    #     return 1
    
    # else:
        
    #     return num * myfactorial(num-1)
    
    return num*myfactorial(num-1) if num > 1 else 1 # more pythonic code

print(myfactorial(5))