import multiprocessing
import time

a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
result = 0


def square():
    global result
    for x in a:
        d = multiprocessing.current_process()
        print("PID = ", d.pid)
        result = x[0]*x[0] + 2*x[0]+x[1] + x[1]*x[1]
        print(result)


if __name__ == '__main__':
    p = multiprocessing.Process(name='square', target=square)

    p.start()
    p.join()
