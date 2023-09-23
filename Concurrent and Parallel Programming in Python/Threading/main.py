import time

from Workers.SleepyWorkers import SleepyWorker
from Workers.SquaredSumWorkers import SquaredSumWorker

def main():
    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        max_value = (i + 1) * 1000000
        squaredSumWorker = SquaredSumWorker(n=max_value)
        current_workers.append(squaredSumWorker)
        # calculate_sum_square((i + 1) * 1000000)

    for thr in current_workers:
        thr.join()

    print("Calculating sum of squares took:", round(time.time() - calc_start_time, 1), "s")

    sleep_start_time = time.time()
    current_workers.clear()

    for seconds in range(1, 6):
        sleepyWorker = SleepyWorker(seconds=seconds)
        current_workers.append(sleepyWorker)
        # sleep_a_little(i)

    for thr in current_workers:
        thr.join()

    print("Sleep took:", round(time.time() - sleep_start_time, 1), "s")

if __name__ == "__main__":
    main()
