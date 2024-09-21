# Mutltithreading
# When to use multi threading
# 1. I/O bound tasks: When the task is waiting for I/O operations like reading file, or network request
# 2. CPU bound tasks: When the task is computationally intensive, but not memory intensive
# 3. GUI applications: When the task is related to GUI, like updating the UI,
# 4. Real-time applications: When the task requires real-time response, like game, or
# 5. Web servers: When the task is related to web server, like handling multiple requests
# Concurrent execution: when you want to improve the throughtput of your appplication

import threading
import time


def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letter():
    for letter in 'ABCDE':
        time.sleep(2)
        print(f"Letter: {letter}")


# created 2 threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)


t_s = time.time()

# print_number()
# print_letter()

# strat the thread
t1.start()
t2.start()

# # wait for the both thread to complete
t1.join()
t2.join()

t_e = time.time()
t_t = t_e - t_s
print(t_t)
