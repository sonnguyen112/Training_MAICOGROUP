def find_greatest_common_divisor (a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def find_least_common_multiple(a, b):
    if a < 0 or b < 0:
        return
    return (a * b) / find_greatest_common_divisor(a, b)


a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
print("Least common multiple of a and b is",find_least_common_multiple(a, b))

