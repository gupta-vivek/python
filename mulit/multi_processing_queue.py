import multiprocessing
import time


def square(n, result):

    for i in n:
        time.sleep(0.5)
        print(multiprocessing.current_process().name)
        result.put(i*i)


def cube(n, result):

    for i in n:
        time.sleep(0.5)
        print(multiprocessing.current_process().name)
        result.put(i*i*i)


if __name__ == '__main__':

    a = [2, 3, 4]

    q_s = multiprocessing.Queue()
    q_c = multiprocessing.Queue()

    p1 = multiprocessing.Process(name='Square', target=square, args=(a, q_s))
    p2 = multiprocessing.Process(name='Cube', target=cube, args=(a, q_c))

    p1.start()
    p2.start()

    p1.join()

    p2.join()

    while q_s.empty() is False:
        print(q_s.get())

    while q_c.empty() is False:
        print(q_c.get())
