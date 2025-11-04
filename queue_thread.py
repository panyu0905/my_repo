#!  /usr/bin/env  python3
import threading, time
import  queue

q  = queue.Queue()

def  Producer():
    n = 0
    while n<5:
        n += 1
        q.put(n)
        print('Producer has created %s\n'  % n)
time.sleep(0.2)
       
def  Consumer():
    count = 0;
    while count<5:
        count += 1
        data = q.get()
        print('Consumer has used % s\n'  % data)
    time.sleep(0.2)
        

if  __name__ == '__main__' :
    p = threading.Thread(target=Producer, name=' ')
    c = threading.Thread(target=Consumer, name=' ')
    p.start()
    
    c.start()
    
    p.join()
    c.join()
