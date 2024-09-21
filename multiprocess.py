# Process that run in parallel
# CPU-bound tasks that are heavy on CPU usage.
# parallel execution: multiple cores of cpu

import multiprocessing
import time


def sqaure_number():
    # Simulate some processing time
    for i in range(5):
        time.sleep(2)
        print(f"square: {i**2}")


def cube_number():
    # Simulate some processing time
    for i in range(5):
        time.sleep(2)
        print(f"square: {i * i * i}")


if __name__ == '__main__':
    # create 2 process
    process1 = multiprocessing.Process(target=sqaure_number)
    process2 = multiprocessing.Process(target=cube_number)

    t_s = time.time()
    # start the process
    process1.start()
    process2.start()
    # wait for the process to finish
    process1.join()
    process2.join()

    t_e = time.time()
    t_t = t_e - t_s
    print(f"Time taken by processes: {t_t} seconds")
