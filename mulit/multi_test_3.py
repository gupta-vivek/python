import multiprocessing
import time

a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]


def square(result):
    for idx, x in enumerate(a):
        d = multiprocessing.current_process()
        print("PID = ", d.pid)
        result[idx] = x[0]*x[0] + 2*x[0]+x[1] + x[1]*x[1]
        print(result[idx])


if __name__ == '__main__':
    result = multiprocessing.Array('i', len(a))
    p = multiprocessing.Process(name='square', target=square, args=(result, ))
    p.start()
    p.join()

    for i in result:
        print(i)