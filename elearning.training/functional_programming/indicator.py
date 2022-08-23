import itertools as it
import time

ind_chars = "\|/-"
indicator = it.cycle(ind_chars)

for _ in range(100):
    print(next(indicator), end='\r')
    time.sleep(0.01)
