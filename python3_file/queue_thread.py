#!  /usr/bin/env  python3
import threading, time
import  queue

q  = queue.Queue()

def  producer():
    n = 0
    while n<5:
        n += 1
        q.put(n)
        print('producer has created %s\n'  % n)
time.sleep(0.2)
       
def  consumer():
    count = 0
    while count<5:
        count += 1
        data = q.get()
        print('consumer has used % s\n'  % data)
    time.sleep(0.2)
        

if  __name__ == '__main__' :
    p = threading.Thread(target=producer, name=' ')
    c = threading.Thread(target=consumer, name=' ')
    p.start()
    
    c.start()
    
    p.join()
    c.join()
