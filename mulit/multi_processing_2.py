import multiprocessing


def square(n, result, v):
    v.value = 8
    for idx, i in enumerate(n):
        result[idx] = i*i

    print("Within process - ", result[:], v.value)


if __name__ == '__main__':
    a = [2, 3, 4]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('i', 7)
    p1 = multiprocessing.Process(target=square, args=(a, result, v))
    p1.start()
    p1.join()
    print("Outside process - ", result[:], v.value)
