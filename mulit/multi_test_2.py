import multiprocessing
import time


def square(x, result):
        result.value = x[0]*x[0] + 2*x[0]+x[1] + x[1]*x[1]
        a = multiprocessing.current_process()
        print(a.pid)

if __name__ == '__main__':

    a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    result = multiprocessing.Value('i', 0)

    for i in a:
        time.sleep(5)
        p = multiprocessing.Process(target=square, args=(i, result))
        p.start()
        p.join()
        print(result.value)
