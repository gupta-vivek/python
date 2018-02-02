import multiprocessing
import time
import math


def square(conn):
    while True:
        i = conn.recv()
        x = i[0] * i[0] + 2 * i[0] * i[1] + i[1] * i[1]
        conn.send(x)


def cube(conn):
    while True:
        i = conn.recv()
        x = math.pow(i[0], 3) + 3 * math.pow(i[0], 2) * i[1] + 3 * i[0] * math.pow(i[1], 2) + math.pow(i[1], 3)
        conn.send(x)


def add(conn):
    while True:
        i = conn.recv()
        x = i[0] + i[1]
        conn.send(x)


if __name__ == '__main__':

    a = [[1, 2], [2, 3]]

    parent_conn_s, child_conn_s = multiprocessing.Pipe()
    parent_conn_c, child_conn_c = multiprocessing.Pipe()
    parent_conn_a, child_conn_a = multiprocessing.Pipe()

    proc_square = multiprocessing.Process(target=square, args=(child_conn_s,))
    proc_square.daemon = True

    proc_cube = multiprocessing.Process(target=cube, args=(child_conn_c, ))
    proc_cube.daemon = True

    proc_add = multiprocessing.Process(target=add, args=(child_conn_a, ))
    proc_add.daemon = True

    proc_square.start()
    proc_cube.start()
    proc_add.start()

    for i in a:
        time.sleep(1)
        parent_conn_s.send(i)
        parent_conn_c.send(i)
        parent_conn_a.send(i)
        print("Square - ", parent_conn_s.recv())
        print("Cube - ", parent_conn_c.recv())
        print("Add - ", parent_conn_a.recv())

    parent_conn_s.close()
    child_conn_s.close()

    parent_conn_c.close()
    child_conn_c.close()

    parent_conn_a.close()
    child_conn_a.close()