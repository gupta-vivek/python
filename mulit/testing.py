import multiprocessing
import time
import os
import psutil


def fun1(conn, pconn):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(10):
            value.append('fun1')
            time.sleep(1)
        # conn.send([pid, value])
        conn.send(value)
        print(pconn.recv())
        print("Function 1 completed.")
        pid.suspend()


def fun2(conn, pconn):
    while True:
        value = []
        pid = psutil.Process(os.getpid())
        for i in range(5):
            value.append('fun2')
            # time.sleep(1)
        # conn.send([pid, value])
        conn.send(value)
        print("Function 2 completed.")
        print(pconn.recv())
        pid.suspend()

if __name__ == '__main__':

    parent_conn1, child_conn1 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=fun1, args=(child_conn1, parent_conn1))

    parent_conn2, child_conn2 = multiprocessing.Pipe()
    p2 = multiprocessing.Process(target=fun2, args=(child_conn2, parent_conn2))

    p1.start()
    p2.start()

    # z1 = parent_conn1.recv()
    # print(z1)
    # # print(z1[1])
    # # z1[0].suspend()
    # #
    # z2 = parent_conn2.recv()
    # print(z2)
    # # print(z2[1])
    # # z2[0].suspend()
    #
    p = psutil.Process(p1.pid)
    p.resume()
    # print(parent_conn1.recv())

