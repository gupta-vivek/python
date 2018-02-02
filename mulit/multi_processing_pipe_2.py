import multiprocessing
import time
"""
def square(conn):
    for x in range(10):
        d = multiprocessing.current_process()
        print("PID = ", d.pid)
        conn.send(x)
        print()
        # result = x[0]*x[0] + 2*x[0]+x[1] + x[1]*x[1]
        # print(result)
"""

def square(conn):
    while True:
        print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    # p = multiprocessing.Process(target=square, args=(child_conn, ))
    # p.start()

    # print(parent_conn.recv())
    a = [[1, 2], [2, 3]]
    p = multiprocessing.Process(target=square, args=(child_conn, ))
    p.start()

    for i in a:
        time.sleep(2)
        parent_conn.send(i)

    # parent_conn.send('hello')
    # print(child_conn.recv())
    # child_conn.send('hi')
    # print(parent_conn.recv())

