import multiprocessing
import time
import os
import psutil

def print_output(q):
    print(q.get())

def fun1(conn):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(10):
            value.append('fun1')
            time.sleep(0.5)
        # conn.send([pid, value])
        conn.put(value)
        print_output(conn)
        # print(value)
        print("Function 1 completed.")
        pid.suspend()


def fun2(conn):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(5):
            value.append('fun2')
            # time.sleep(1)
        # conn.send([pid, value])
        conn.put(value)
        print_output(conn)
        # print(value)
        print("Function 2 completed.")
        pid.suspend()

if __name__ == '__main__':

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=fun1, args=(q, ))

    p2 = multiprocessing.Process(target=fun2, args=(q, ))

    # p3 = multiprocessing.Process(target=fun3, args=(q, ))

    p1.start()
    p2.start()
    # p3.start()

    # p1.join()
    # p2.join()

    time.sleep(10)

    p = psutil.Process(p1.pid)
    p.resume()

    p = psutil.Process(p2.pid)
    p.resume()