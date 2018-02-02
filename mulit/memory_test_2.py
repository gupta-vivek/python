import multiprocessing
import time
import math
import os
import psutil


def test(conn):
    print("Hello from function")
    print(conn.recv())


def make_proc(func):
    print("Hello from make process")
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=func, args=(child_conn, ))
    # p.daemon = True
    # p.start()

    return {
        'p': p,
        'pid': p.pid,
        'parent_conn': parent_conn,
        'child_conn': child_conn
    }


def proc_status(pid):
    proc = psutil.Process(pid)
    proc_mem = proc.memory_info()[0] / float(2 ** 20)
    proc_cpu = proc.cpu_times()[0]

    return {
        'mem_usage': proc_mem,
        'cpu_usage': proc_cpu
    }


if __name__ == '__main__':

    test_fun = make_proc(test)
    # test_fun['p'].daemon = True
    test_fun['p'].start()
    test_fun['parent_conn'].send('Hello from pipe')
    test_fun_stat = proc_status(test_fun['pid'])
    print(test_fun_stat)