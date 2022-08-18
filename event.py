import asyncio

def random_func(loop):
    print("Inside random function")
    loop.stop()
    
loop = asyncio.get_event_loop()
loop.call_soon(random_func,loop)
loop.run_forever()
loop.close()

