import asyncio

# async def main():
    
#         print("Hello..")
#         await asyncio.sleep(2)
#         print("Hello after 2 seconds")
    
# asyncio.run_forever(main())  
#=====================================================
# Tech with Tim
#---------------
# 1. for writing asynchronous code we need to write a coroutine
# 2. and that is written with the async keyword befor the function name
# 3. next we need to define an event loop and execute it. 
# 4. create task for non writing non blocking code. 

# async def main():
#     await asyncio.sleep(2)
#     print("main is called")
    
# async def main_caller(): 
#     print("main caller is called")
#     await main()
#     print("call to main has been made but it will not execute until main finishes ")
    
# asyncio.run(main_caller())
#++++++++++++++++++++++++++++++++++++++++++++++++
# async def main():
#     await asyncio.sleep(2)
#     print("main is called , I will execute at the last even though I was 2nd in posiion")
    
# async def main_caller(): 
#     print("main caller is called")
#     task = asyncio.create_task(main()) 
#     print("call to main has been made, main will take 2 seconds but this will execute before main finishes to run ")
     
# asyncio.run(main_caller())
#+++++++++++++++++++++++++++++++++++++++++++++++++
# async def main():
#     await asyncio.sleep(2)
#     print("main is called , I will execute at the 2nd posiion")
    
# async def main_caller(): 
#     print("main caller is called")
#     task = asyncio.create_task(main()) 
#     await task
#     print("call to main has been made,Now I will execute at the last ")
     
# asyncio.run(main_caller())
#+++++++++++++++++++++++++++++++++++++++++++++++++

# async def main():
    
#     await asyncio.sleep(2)
    
#     print("main is called , I will execute at the 2nd in posiion")
    
# async def main_caller(): 
    
#     print("main_caller is called")
    
#     task = asyncio.create_task(main()) 
    
#     await asyncio.sleep(4)
    
#     print("call to main has been made, main will take 2 seconds but this , I will execute at the last ")
     
# asyncio.run(main_caller())

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

async def main():
    
    print("main is called , I will execute at 2ND PLACE")
    
    await asyncio.sleep(4)
    print( "4 seconds completed ")    # This line doesn't get printed is await is not written at
#-                                      at the last in main_calller
    
async def main_caller(): 
    
    print("main_caller is called")
    
    task = asyncio.create_task(main()) 
    
    await asyncio.sleep(2)
    
    print("call to main has been made, main will take 4 seconds but this , I will execute at LAST")
    
    await task
     
asyncio.run(main_caller())