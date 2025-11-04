#! /usr/bin/env python3

import multiprocessing
import time

s = multiprocessing.Semaphore(2)
def process1():
    s.acquire()
    print('process1 acquire and it will sleep 5s')
    time.sleep(5)
    print('process1 release')
    s.release()

def process2():
    s.acquire()
    print('process2 acquire and it will sleep 5s')
    time.sleep(5)
    print('process2 release')
    s.release()

def process3():
    print('process3 try to start')
    # 添加超时机制，避免永久阻塞
    if s.acquire(timeout=10):  # 等待最多10秒
        print('process3 acquire and it will sleep 5s')
        time.sleep(5)
        print('process3 release')
        s.release()
    else:
        print('process3 failed to acquire semaphore within timeout')

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p3 = multiprocessing.Process(target=process3)
    
    p1.start()
    time.sleep(1)
    p2.start()
    time.sleep(1)
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    print("All processes completed")
