import asyncio

# async def main():
    
#         print("\nHello..\n")
#         await asyncio.sleep(2)
#         print("\nHello after 2 seconds\n")
    
# asyncio.run_forever(main())  

#=====================================================
# Tech with Tim
#---------------
# 1. for writing asynchronous code we need to write a coroutine
# 2. and that is written with the async keyword befor the function name
# 3. next we need to define an event loop and execute it. 
# 4. create task for writing non blocking code. 

# async def main():
#     await asyncio.sleep(2)
#     print("\nmain is called\n")
    
# async def main_caller(): 
#     print("\nmain caller is called\n")
#     await main()
#     print("\ncall to main has been made but it will not execute until main finishes \n")
    
# asyncio.run(main_caller())

#++++++++++++++++++++++++++++++++++++++++++++++++

# ************** C R E A T I N G   T A S K *****************8**

async def main():

    await asyncio.sleep(2)
    print("\nmain is called , I will execute at the last even though I was 2nd in posiion\n")
    
async def main_caller(): 

    print("\nmain caller is called\n")
    task = asyncio.create_task(main()) 
    print("\ncall to main has been made, main will take 2 seconds but this will execute before main finishes to run \n")
     
asyncio.run(main_caller())

#+++++++++++++++++++++++++++++++++++++++++++++++++

# async def main():
#     await asyncio.sleep(2)
#     print("\nmain is called , I will execute at the 2nd posiion\n")
    
# async def main_caller(): 
#     print("\nmain caller is called\n")
#     task = asyncio.create_task(main()) 
#     await task
#     print("\ncall to main has been made,Now I will execute at the last \n")
     
# asyncio.run(main_caller())
#+++++++++++++++++++++++++++++++++++++++++++++++++

# async def main():
    
#     await asyncio.sleep(2)
    
#     print("\nmain is called , I will execute at the 2nd in posiion\n")
    
# async def main_caller(): 
    
#     print("\nmain_caller is called\n")
    
#     task = asyncio.create_task(main()) 
    
#     await asyncio.sleep(4)
    
#     print("\ncall to main has been made, main will take 2 seconds but this , I will execute at the last \n")
     
# asyncio.run(main_caller())

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# async def main():
    
#     print("\nmain is called , I will execute at 2ND PLACE\n")
    
#     await asyncio.sleep(4)
    
#     print( "4 seconds completed \n")    # This line doesn't get printed is await is not written at
# #-                                      at the last in main_calller
    
# async def main_caller(): 
    
#     print("\nmain_caller is called\n")
    
#     task = asyncio.create_task(main()) 
    
#     await asyncio.sleep(2)
    
#     print("\ncall to main has been made, main will take 4 seconds but this , I will execute at LAST\n")
    
#     await task
     
# asyncio.run(main_caller())