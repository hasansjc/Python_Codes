# import asyncio


# def random_func(loop):
#     print("Inside random function")
#     loop.stop()
    
# loop = asyncio.get_event_loop()
# loop.call_soon(random_func,loop)
# loop.run_forever()
# loop.close()
# Importing asyncio module in the program  
import asyncio  
# A default function with event loops method  
def loopText(loop):  
   # A text printing command  
       print('Printing this text through the event loop')  
       loop.stop() # Stopping the loop  
loop = asyncio.get_event_loop() # Using get_event_loop() method to print the text  
loop.call_soon(loopText, loop) # Using call_soon() method from event loops  
loop.run_forever() # run_forever() on event loop  
loop.close() # Closing the loop  