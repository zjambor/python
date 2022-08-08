import queue
import random
import threading
import time

class AddMulThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            try:
                p = self.queue.get(timeout=1)
                add_mul(*p)
            except queue.Empty:
                break

def rand_pair(min, max):
    return random.randint(min, max), random.randint(min, max)

def add_mul(a, b):
    sum_a_b = a + b
    mul_a_b = a * b

q = queue.Queue()

for _ in range(100000):
    q.put(rand_pair(1, 100000))

def addmultest():
    threads = []
    for _ in range(4):
        t = AddMulThread(q)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

start = time.time()
addmultest()
end = time.time()
print(f"Took {end - start:3.3f} sec to test parallel 1000000 values")
