import time
import concurrent.futures

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName}: {time.ctime(time.time())}")

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # args = (("Thread-1", 1.5), ("Thread-2", 1.8)) 
    args = ((f"Thread-{i}", i) for i in range(1, 3))     # generator
    # print(*args)        # ('Thread-1', 1) ('Thread-2', 2)
    # print(*zip(*args))      # ('Thread-1', 'Thread-2') (1, 2)
    executor.map(print_time, *zip(*args))
