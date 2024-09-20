# MultiThreading & MultiProcessing

==============================

### Key Concepts:

- Program
- Process
- Thread
- Multi-Threading
- Multi-Processing

### Key Terms:

- **Process**: A program in execution, including the memory space, open files, and other resources
- **Thread**: A flow of execution within a process
- **Multi-Threading**: A process that can have multiple threads of execution, allowing for concurrent execution
- **Multi-Processing**: A system that can run multiple processes concurrently, allowing for parallel execution

### Key Questions:

1. What is the difference between a process and a thread?

   - **_Process:_** A process is a program in execution, and it has its own memory space, resources, and execution environment. Processes are independent of each other.
   - **_Thread:_** A thread is the smallest unit of execution within a process. Multiple threads can exist within the same process and share the same memory space, allowing for more efficient communication.

2. What is the main advantage of multi-threading over multi-processing?

   - Threads share the same memory space, which makes communication between threads faster and more efficient than between processes. In multi-processing, each process has its own separate memory space, requiring more overhead to communicate between processes (e.g., through inter-process communication).

3. How do you create and manage threads in Python?
   - You can create threads using the threading module in Python. Example:

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

# Creating a thread
thread = threading.Thread(target=print_numbers)
thread.start()

# Waiting for the thread to finish
thread.join()
```

4. How do you create and manage processes in Python?
   - You can create processes using the multiprocessing module. Example:

```python
import multiprocessing

def print_numbers():
for i in range(10):
print(i)

# Creating a process

process = multiprocessing.Process(target=print_numbers)
process.start()

# Waiting for the process to finish

process.join()

```
