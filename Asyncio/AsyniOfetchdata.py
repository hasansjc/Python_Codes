import asyncio

async def fetch_data():
    
    print('start fetching')
    
    await asyncio.sleep(2)
    
    print('done fetching')
    
    return { 'data': 1 }

async def print_numbers():
    
    for i in range(10):
        
        print(i)
        
        await asyncio.sleep(1)
        
async def main():
    
    task1 = asyncio.create_task(fetch_data())
    
    task2 = asyncio.create_task(print_numbers())
    
    value1 = await task1
   
    print("value1 === ",value1)
    
    value2 = await task2
     
asyncio.run(main())