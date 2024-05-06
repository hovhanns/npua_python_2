import concurrent.futures
import threading

# Define a function that will be executed by the worker threads
def task(name):
    print(f"Executing task {name} in thread {threading.current_thread().name}")

# Create a thread pool with a maximum of 5 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the thread pool
    executor.submit(task, "Task 1")
    executor.submit(task, "Task 2")
    executor.submit(task, "Task 3")
    executor.submit(task, "Task 4")
    executor.submit(task, "Task 5")