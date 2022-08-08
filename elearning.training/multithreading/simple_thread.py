import threading
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName}: {time.ctime(time.time())}")

t = threading.Thread( target=print_time, args=("Thread-1", 1.5), daemon=False)
threading.Thread( target=print_time, args=("Thread-2", 1.8), daemon=False).start()

t.start()
t.join()
