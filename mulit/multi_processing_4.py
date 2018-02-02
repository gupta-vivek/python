import multiprocessing
import time
import math


def square(conn, lock):
    while True:
        lock.acquire()
        i = conn.recv()
        x = i[0] * i[0] + 2 * i[0] * i[1] + i[1] * i[1]
        conn.send(x)
        lock.release()


def cube(conn, lock):
    while True:
        lock.acquire()
        i = conn.recv()
        x = math.pow(i[0], 3) + 3 * math.pow(i[0], 2) * i[1] + 3 * i[0] * math.pow(i[1], 2) + math.pow(i[1], 3)
        conn.send(x)
        lock.release()


def add(conn, lock):
    while True:
        lock.acquire()
        i = conn.recv()
        x = i[0] + i[1]
        conn.send(x)
        lock.release()


if __name__ == '__main__':

    a = [[1, 2], [2, 3]]

    parent_conn, child_conn = multiprocessing.Pipe()

    lock = multiprocessing.Lock()

    proc_square = multiprocessing.Process(target=square, args=(child_conn, lock))
    proc_square.daemon = True

    proc_cube = multiprocessing.Process(target=cube, args=(child_conn, lock))
    proc_cube.daemon = True

    proc_add = multiprocessing.Process(target=add, args=(child_conn, lock))
    proc_add.daemon = True

    proc_square.start()
    proc_cube.start()
    proc_add.start()

    for i in a:
        time.sleep(2)
        parent_conn.send(i)
        parent_conn.send(i)
        parent_conn.send(i)
        print("Square - ", parent_conn.recv())
        print("Cube - ", parent_conn.recv())
        print("Add - ", parent_conn.recv())

    parent_conn.close()
    child_conn.close()