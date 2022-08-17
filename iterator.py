l1 = [10,20,30,40,50]

# myiter = iter(l1)

# myiter = l1.__iter__()  Does not work this way 

print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())  
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())

# for i in range(5):
#     print(myiter.__next__())
# print("end of for loop")
# print("_____________________________") 
# while True:
#     try:
#         # print(myiter.__next__())  # Both the methods work 
#         print(next(myiter)) 
#     except:
#         StopIteration
#         break
# for i in l1: 
#     print(i)
