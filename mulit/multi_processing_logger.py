import multiprocessing
import logging


def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':

    items = ['ha', 'haha', 'hahaha']
    lock = multiprocessing.Lock()

    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    for item in items:
        p = multiprocessing.Process(target=printer, args=(item, lock))
        p.start()