def draw_triangle_star(n):
    if n < 0:
        return
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i * 2 - 1):
            print("*", end="")
        print()


n = int(input("Nhap n: "))
draw_triangle_star(n)
