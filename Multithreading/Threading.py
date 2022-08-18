import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print('done')
    
x = threading.Thread(target=func)  # (target = func, args =() )Args is a tuple and for a single value we need to add , at the  end eg. (4,)

x.start()
print(threading.active_count())
    