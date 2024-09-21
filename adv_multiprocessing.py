# Multiprocessing with processpoolexecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
    time.sleep(1)  # Simulate some work
    return f'Square : {number ** 2}'


numbers = [1, 2, 3, 4, 5]
start_time = time.time()
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for re in results:
        print(re)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
