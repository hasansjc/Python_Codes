import time

def mycoroutine():
    text = "This is any random text which has 9 wordds."
    time.sleep(2)
    
    while True:
        input = (yield)
        if input in text:
            print("Your text exist")
        else: 
            print(" Your text does not exist")
    
    
search = mycoroutine()
next(search)
search.send("texx")    
search.close()
