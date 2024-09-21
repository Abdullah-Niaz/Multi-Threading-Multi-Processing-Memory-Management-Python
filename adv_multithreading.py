# Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time


def print_number(number):
    time.sleep(1)
    return f'Number: {number}'


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a ThreadPoolExecutor with 3 worker threads

t_s = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_number, numbers)
    # Submit tasks to the executor
    # futures = [executor.submit(print_number, number) for number in numbers]

for result in result:
    print(result)

t_e = time.time()

t_t = t_e - t_s
print(t_t)
