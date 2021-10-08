import numpy as np
import sympy as sp


def multiplication_2_matrix(matrix1, matrix2):
    return matrix1 @ matrix2


def odd_even_matrix(matrix):
    matrix[matrix % 2 == 0] = 1
    matrix[matrix != 1] = 0
    return matrix


def flip_matrix(matrix):
    return np.fliplr(matrix)


def count_prime_diagonal(matrix):
    diagonal = matrix.diagonal()
    vfunc = np.vectorize(sp.isprime)
    return np.count_nonzero(vfunc(diagonal))


def main():
    print("a)")
    A = np.random.randint(20, size=(3, 4))
    B = np.random.randint(20, size=(4, 4))
    product = multiplication_2_matrix(A, B)
    print(A, "\n x ")
    print(B, "\n = ")
    print(product, "\n")

    print("b)")
    A = np.random.randint(20, size=(4, 4))
    print("Before: \n", A)
    A = odd_even_matrix(A)
    print("After: \n", A, "\n")

    print("c)")
    A = np.random.randint(20, size=(5, 5))
    print("A before flip: \n", A)
    A = flip_matrix(A)
    print("A after flip: \n", A)
    print(f"The number of prime is: {count_prime_diagonal(A)}")


if __name__ == "__main__":
    main()
