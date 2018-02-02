import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print("Hello from class.")
        return

if __name__ == '__main__':
    p = Worker()
    p.start()
