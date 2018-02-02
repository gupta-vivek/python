import multiprocessing
import time
import math
import os
import psutil


def test_fun(conn):
    while True:
        print(conn.recv())


def mkproc(func):
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=func, args=(child_conn,))
    p.daemon = True
    p.start()

    return {
        'pid': p.pid,
        'parent_conn': parent_conn,
        'child_conn': child_conn
    }


def proc_status(pid):
    proc = psutil.Process(pid)
    proc_mem = proc.memory_info()[0] / float(2 ** 20)

    return {
        'mem_usage': proc_mem
    }


def square(conn):
    while True:
        i = conn.recv()
        square_pid = multiprocessing.current_process().pid
        square_mem = psutil.Process(square_pid)
        # mem = square_mem.memory_info()[0] / float(2 ** 20)
        mem = square_mem.memory_info()
        print("Memory - ", mem)
        # print(square_mem.memory_info().rss)
        x = i[0] * i[0] + 2 * i[0] * i[1] + i[1] * i[1]
        conn.send(x)


def cube(conn):
    while True:
        i = conn.recv()
        p = psutil.Process()
        print(p)
        x = math.pow(i[0], 3) + 3 * math.pow(i[0], 2) * i[1] + 3 * i[0] * math.pow(i[1], 2) + math.pow(i[1], 3)
        conn.send(x)


def add(conn):
    while True:
        i = conn.recv()
        print(psutil.Process())
        x = i[0] + i[1]
        conn.send(x)


if __name__ == '__main__':

    a = [[1, 2], [2, 3]]
    square_fun = mkproc(test_fun)
    square_fun['parent_conn'].send([1, 2])
    # print(square_fun['child_conn'].recv())