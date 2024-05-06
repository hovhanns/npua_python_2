import multiprocessing

def worker(num):
    """Worker function"""
    model = "loaded model" # 5GB
    result = num * num
    if num == 0:
        raise ValueError("An error occurred")
    print(f"Result: {result}")


if __name__ == "__main__":
    # Number of processes to create
    num_processes = 4

    # Create a list of processes
    processes = []
    
    # Create and start the processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()