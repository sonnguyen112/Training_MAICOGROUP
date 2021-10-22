import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_csv(file_path):
    return pd.read_csv(file_path)


def is_stop(old_label, new_label):
    return np.array_equal(old_label, new_label)


def PLA(w_init, points, label):
    X = points
    y = label
    y[y == 0] = -1
    numOfPoints = points.shape[1]
    w = w_init
    while True:
        mix_id = np.random.permutation(numOfPoints)
        for i in range(numOfPoints):
            x_i = X[:, mix_id[i]].reshape(X.shape[0], 1)
            if np.sign(w.T @ x_i)[0] != y[mix_id[i]]:
                w = w + y[i]*x_i
        if is_stop(y.reshape(1, len(y)), np.sign(w.T @ X)):
            break
    return w


def draw_line(w):
    w0, w1, w2 = w[0], w[1], w[2]
    if w2 != 0:
        x11, x12 = -300, 300
        return plt.plot([x11, x12], [-(w1*x11 + w0)/w2, -(w1*x12 + w0)/w2], 'b-')
    else:
        x10 = -w0/w1
        return plt.plot([x10, x10], [-300, 300], 'b-')


def visualize(df, w):
    w_0, w_1, w_2 = w[0, 0], w[1, 0], w[2, 0]
    plt.plot(df["x"].values[df["label"] == -1], df["y"].values[df["label"] == -1],
             "bo", df["x"].values[df["label"] == 1], df["y"].values[df["label"] == 1], "ro")
    draw_line(w)
    plt.show()


def main():
    np.random.seed(42)
    df = load_csv("datasets/PLA.csv")
    X = np.concatenate((df["x"].values.reshape(1, len(
        df["x"].values)), df["y"].values.reshape(1, len(df["y"].values))), axis=0)
    X_bar = np.concatenate((np.ones((1, X.shape[1])), X))
    label = df["label"].values
    label[label == 0] = -1
    w_init = np.random.randn(X_bar.shape[0], 1)
    w = PLA(w_init, X_bar, label)
    print(f"w0 = {w[0,0]}, w1 = {w[1,0]}, w2 = {w[2,0]}")
    visualize(df, w)


if __name__ == "__main__":
    main()
