from threading import Thread
import random
import time
import concurrent.futures

number_of_cores = 4

def calculate(num_a, num_b):
    return (num_a + num_b, num_a * num_b)

def test_calc():
    for _ in range(1000000):
        num_a = random.randint(0,100)
        num_b = random.randint(0,100)
        calculate(num_a, num_b)

start = time.time()
for i in range(number_of_cores):
    test_calc()
    print(f"section {i} finished")
end = time.time()
print(f"Took {end - start:3.3f} sec to test 1000000 values")

threads = []

start = time.time()
for _ in range(number_of_cores):
    t = Thread(target=test_calc)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    print("thread finished")
end = time.time()
print(f"Took {end - start:3.3f} sec to test parallel 1000000 values")

start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(test_calc)
end = time.time()
print(f"Took {end - start:3.3f} sec to test parallel 1000000 values with executor")
