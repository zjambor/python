from multiprocessing import Process, Queue
import queue
from isprime import is_prime
import time

class PrimeChecker(Process):

    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        Process.__init__(self)

    def run(self):
        while self.flag:
            try:
                n = self.queue.get(timeout=1)
                is_prime(n)
            except queue.Empty:
                break

def test_primes():
    numbers = [1397337, 1116281, 104395303, 472882027, 533000389, 817504243, 982451653, 112272535095283, 115280095190773, 1099726899285419]*5

    q = Queue(100)

    for n in numbers:
        q.put(n)

    processes = []
    for _ in range(4):
        p = PrimeChecker(q)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    start = time.time()
    test_primes()
    end = time.time()
    print(f"Took {end - start:3.3f} sec to check primes")
