import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(1, 5)
y1 = [1, 4, 3, 9]
x2 = np.arange(1, 6)
y2 = [1, 6, 2, 3, 9]
plt.plot(x1, y1, "r-", x2, y2, "g^")
plt.xlabel("Hoành độ")
plt.ylabel("Tung độ")
plt.title("ABC")
plt.show()

x = np.arange(1, 5)
y1 = [50, 100, 200, 10]
y2 = [85, 25, 20, 35]
plt.bar(x - 0.1, y1, 0.2, label = '1', color = "green")
plt.bar(x + 0.1, y2, 0.2, label = '2', color = "yellow")
plt.xticks(x, x)
plt.legend()
plt.title("Bar")
plt.show()

fig, ax = plt.subplots(nrows=2, ncols=2)
x1 = np.arange(1, 5)
y1 = [1, 4, 3, 9]
x2 = np.arange(1, 6)
y2 = [1, 6, 2, 3, 9]
x4 = [1, 2, 4]
y4 = [1, 5, 1]
ax[0, 0].plot(x1, y1, "g-")
ax[0, 1].plot(x2, y2, "r-")
ax[1, 1].plot(x4, y4, "y-")
ax[0, 0].set_title("abc1")
ax[0, 1].set_title("abc2")
ax[1, 0].set_title("abc3")
ax[1, 1].set_title("abc4")
plt.suptitle("abc")
plt.show()