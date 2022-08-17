l1 = [1,2,3,4,5,6,7,8,9]


def is_greater_than_5(num):
    return num>5
    

num_greater_than_5 = list(filter(is_greater_than_5, l1))

print(num_greater_than_5)