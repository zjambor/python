import time
import threading

def calculate_sum_square(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        max_value = (i + 1) * 1000000
        t = threading.Thread(target=calculate_sum_square, args=(max_value, ))
        t.start()
        current_threads.append(t)
        # calculate_sum_square((i + 1) * 1000000)

    for thr in current_threads:
        thr.join()

    print("Calculating sum of squares took:", round(time.time() - calc_start_time, 1), "s")

    sleep_start_time = time.time()
    current_threads.clear()

    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds, ))
        t.start()
        current_threads.append(t)
        # sleep_a_little(i)

    for thr in current_threads:
        thr.join()

    print("Sleep took:", round(time.time() - sleep_start_time, 1), "s")

if __name__ == "__main__":
    main()
