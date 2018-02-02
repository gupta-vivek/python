import multiprocessing
import time

def wait_for_event(e):
    print("Wait for event: starting", )
    e.wait()
    print("Wait for event: e.is_set()", e.is_set())

def wait_for_event_timeout(e, t):
    print("Wait for event timeout: starting")
    e.wait(t)
    print("Wait for event timeout: e.is_set()", e.is_set())

if __name__ == "__main__":
    e = multiprocessing.Event()
    p1 = multiprocessing.Process(target=wait_for_event, args=(e, ))
    p1.start()
    p2 = multiprocessing.Process(target=wait_for_event_timeout, args=(e, 2))
    p2.start()

    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print("E value1: ", e.is_set())
    e.clear()
    print("E value2: ", e.is_set())
    print('main: event is set')
