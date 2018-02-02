import multiprocessing


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=f, args=(child_conn, ))
    p1.start()
    p1.join()
    print(parent_conn.recv())
