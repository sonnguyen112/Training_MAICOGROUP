import numpy as np
import sympy as sp
A = np.random.randint(20, size = (3, 4))
B = np.random.randint(20, size = (4, 4))
print(A @ B)

A = np.random.randint(20, size = (4, 4))
A[A % 2 == 0] = 1
A[A != 1] = 0
print(A)

A = np.random.randint(20, size = (5, 5))
A = np.fliplr(A)
A_diagonal = A.diagonal()
vfunc = np.vectorize(sp.isprime)
print(f"The number of prime is: {np.count_nonzero(vfunc(A_diagonal))}")