import multiprocessing
import time


def square(n):
    for i in n:
        time.sleep(1)
        print("Square")
        print(i*i)


def cube(n):
    for i in n:
        time.sleep(1)
        print("Cube")
        print(i*i*i)


if __name__ == "__main__":
    a = [2, 3, 4]
    p1 = multiprocessing.Process(target=square, args=(a,))
    p2 = multiprocessing.Process(target=cube, args=(a,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print("Hello")