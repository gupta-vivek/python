import multiprocessing
import math
import psutil
from subprocess import check_output, STDOUT

all_pro = []
all_conn = []


def test(conn):
    print("Hello from function")
    print(conn.recv())


def square(conn):
    while True:
        i = conn.recv()
        x = i[0] * i[0] + 2 * i[0] * i[1] + i[1] * i[1]
        conn.send(x)


def cube(conn):
    while True:
        i = conn.recv()
        x = math.pow(i[0], 3) + 3 * math.pow(i[0], 2) * i[1] + 3 * i[0] * math.pow(i[1], 2) + math.pow(i[1], 3)
        conn.send(x)


def add(conn):
    while True:
        i = conn.recv()
        x = i[0] + i[1]
        conn.send(x)


def make_proc(func):
    print("Hello from make process")
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=func, args=(child_conn,))
    all_pro.append(p.pid)
    all_conn.append(parent_conn)
    all_conn.append(child_conn)
    # p.daemon = True
    p.start()

    return {
        'p': p,
        'pid': p.pid,
        'parent_conn': parent_conn,
        'child_conn': child_conn
    }


def proc_status(pid):
    proc = psutil.Process(pid)
    # proc_mem = proc.memory_info()[0] / float(2 ** 20)
    proc_mem = proc.memory_full_info()[7] / float(
        2 ** 20)  # Returns the amount of memory that will be freed when this process is terminated.
    proc_mem_percent = proc.memory_percent(memtype='uss')
    proc_threads = proc.num_threads()

    return {
        'mem_usage': proc_mem,
        'mem_percentage': proc_mem_percent,
        'num_threads': proc_threads,
    }


def get_ram_usage():
    total_memory = psutil.virtual_memory()[0] / float(2 ** 30)
    used_memory = psutil.virtual_memory()[3] / float(2 ** 30)
    free_memory = psutil.virtual_memory()[4] / float(2 ** 30)
    used_percent = psutil.virtual_memory()[2]
    free_percent = 100.0 - used_percent

    ram_usage = {
        'total_memory': "{0:.2f}".format(total_memory),
        'used_memory': "{0:.2f}".format(used_memory),
        'free_memory': "{0:.2f}".format(free_memory),
        'used_percent': used_percent,
        'free_percent': free_percent
    }

    return ram_usage


def get_disk_usage():
    total = psutil.disk_usage('/')[0] / float(2 ** 30)
    used = psutil.disk_usage('/')[1] / float(2 ** 30)
    free = psutil.disk_usage('/')[2] / float(2 ** 30)
    percent = psutil.disk_usage('/')[3]

    disk_usage = {
        'total:': "{0:.2f}".format(total),
        'used': "{0:.2f}".format(used),
        'free': "{0:.2f}".format(free),
        'percent': percent
    }

    return disk_usage


def get_cpu_usage():
    cpu_usage = float(str(
        check_output("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'",
                     stderr=STDOUT, shell=True), encoding="utf-8"))
    cpu_usage = {
        'used': "{0:.2f}".format(cpu_usage),
        'free': "{0:.2f}".format(100.0 - cpu_usage)
    }
    return cpu_usage


if __name__ == '__main__':

    square_fun = make_proc(square)
    cube_fun = make_proc(cube)
    add_fun = make_proc(add)

    a = [[1, 1], [2, 2], [3, 3]]
    for i in a:
        square_fun['parent_conn'].send(i)
        print("Square - ", square_fun['parent_conn'].recv())

        cube_fun['parent_conn'].send(i)
        print("Cube - ", cube_fun['parent_conn'].recv())

        add_fun['parent_conn'].send(i)
        print("Add - ", add_fun['parent_conn'].recv())

    print(get_ram_usage())
    print(get_disk_usage())
    print(get_cpu_usage())

    # Close the connections.
    for conn in all_conn:
        conn.close()

    # Terminate the processes.
    for proc in all_pro:
        proc = psutil.Process(proc)
        proc.terminate()