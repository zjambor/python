import numpy as np
from numba import vectorize
import time

def Add(a, b):
    return a + b

@vectorize(['float32(float32, float32)'], target='cuda')
def Add_gpu(a, b):
    return a + b

# Initialize arrays
N = 300000000
A = np.ones(N, dtype=np.float32)
B = np.ones(A.shape, dtype=A.dtype)
C = np.empty_like(A, dtype=A.dtype)

start = time.time()
C = Add(A, B)
end = time.time()
print("\nC=", C, "\nComputation lasted:", str(end-start))

start = time.time()
# Add arrays on GPU
C = Add_gpu(A, B)
end = time.time()
print("\nC=", C, "\nComputation lasted:", str(end-start))
