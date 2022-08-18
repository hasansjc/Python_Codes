import threading
import time
def count1(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)
        
def count2(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)
        
x = threading.Thread(target=count1, args=(10,))

x.start()

y = threading.Thread(target=count2, args=(10,))

y.start()

print('done')

