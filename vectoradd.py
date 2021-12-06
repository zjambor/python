import numpy as np
import math
from timeit import default_timer as timer
import time
from numba import vectorize, cuda

@vectorize(['float32(float32, float32, float32)'], target='cuda')
def VectorAdd(a, b, c):
    return a + b

    # for i in range(0,32000000):
    #     c[i] = a[i] + b[i]
    # return c

@vectorize(['float32(float32, float32, float32)',
            'float64(float64, float64, float64)'],
           target='cuda')
def cu_discriminant(a, b, c):
    return math.sqrt(b ** 2 - 4 * a * c)

def main():
    # N = 22000000

    # A = np.ones(N, dtype=np.float32)
    # B = np.ones(N, dtype=np.float32)
    # C = np.zeros(N, dtype=np.float32)

    # start = time.time()
    # C = VectorAdd(A,B,C)
    # vectoradd_time = time.time() - start
    # print("C[:5] = " + str(C[:5]))
    # print("C[-5:] = " + str(C[-5:]))

    # print("VerctorAdd took %f seconds" % vectoradd_time)

    N = 10000000
    dtype = np.float32

    # prepare the input
    A = np.array(np.random.sample(N), dtype=dtype)
    B = np.array(np.random.sample(N) + 10, dtype=dtype)
    C = np.array(np.random.sample(N), dtype=dtype)

    start = time.time()
    D = cu_discriminant(A, B, C)
    vectoradd_time = time.time() - start

    print(D)  # print result
    print("cu_discriminant took %f seconds" % vectoradd_time)

if __name__ == '__main__':
    main()