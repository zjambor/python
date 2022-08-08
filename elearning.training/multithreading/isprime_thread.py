from threading import Thread
import queue
from isprime import is_prime
import time

class PrimeChecker(Thread):

    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        Thread.__init__(self)

    def run(self):
        while self.flag:
            try:
                n = self.queue.get(timeout=1)
                is_prime(n)
            except queue.Empty:
                break

def test_primes():
    numbers = [1397337, 1116281, 104395303, 472882027, 533000389, 817504243, 982451653, 112272535095283, 115280095190773, 1099726899285419]*5

    q = queue.Queue(100)

    for n in numbers:
        q.put(n)

    threads = []
    for _ in range(4):
        t = PrimeChecker(q)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

start = time.time()
test_primes()
end = time.time()
print(f"Took {end - start:3.3f} sec to check primes")
