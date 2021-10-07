import numpy as np
import sympy as sp


def product_rand_matrix():
    print("a)")
    A = np.random.randint(20, size=(3, 4))
    B = np.random.randint(20, size=(4, 4))
    print(A, "\n x ")
    print(B, "\n = ")
    print(A @ B, "\n")


def odd_even_matrix():
    print("b)")
    A = np.random.randint(20, size=(4, 4))
    print("Before: \n", A)
    A[A % 2 == 0] = 1
    A[A != 1] = 0
    print("After: \n", A, "\n")


def flip_and_count_prime_diagonal():
    print("c)")
    A = np.random.randint(20, size=(5, 5))
    print("A before flip: \n", A)
    A = np.fliplr(A)
    print("A after flip: \n", A)
    A_diagonal = A.diagonal()
    vfunc = np.vectorize(sp.isprime)
    print(f"The number of prime is: {np.count_nonzero(vfunc(A_diagonal))}")


product_rand_matrix()
odd_even_matrix()
flip_and_count_prime_diagonal()
