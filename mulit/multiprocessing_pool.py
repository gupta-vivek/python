from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == '__main__':

    p = Pool()
    a = [1, 2, 3, 4]
    result = p.map(f, a)
    print(result)