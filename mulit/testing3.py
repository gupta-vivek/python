import multiprocessing
import time
import os
import psutil


def print_output(q):
    print(q.get())


def fun1(q):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(q.get()):
            value.append('fun1')
            time.sleep(0.5)
        q.put(value)
        print_output(q)
        print("Function 1 completed.")
        pid.suspend()


def fun2(q):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(q.get()):
            value.append('fun2')
        q.put(value)
        print_output(q)
        print("Function 2 completed.")
        pid.suspend()

if __name__ == '__main__':

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=fun1, args=(q, ))
    p2 = multiprocessing.Process(target=fun2, args=(q, ))

    q.put(5)
    p1.start()
    q.put(10)
    p2.start()

    time.sleep(10)

    q.put(5)
    p = psutil.Process(p1.pid)
    p.resume()

    q.put(5)
    p = psutil.Process(p2.pid)
    p.resume()