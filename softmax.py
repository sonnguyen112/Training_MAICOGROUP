import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics import accuracy_score


def load_csv(file_path):
    return pd.read_csv(file_path)


def softmax_stable(Z):
    e_Z = np.exp(Z - np.max(Z, axis=0, keepdims=True))
    A = e_Z / e_Z.sum(axis=0)
    return A


def convert_labels(label, numberOfClass):
    y = label
    Y = sparse.coo_matrix((np.ones_like(y),
                           (y, np.arange(len(y)))), shape=(numberOfClass, len(y))).toarray()
    return Y


def softmax_regression(X_bar, y, W_init, eta, max_count=10000):
    C = y.max() + 1  # Num of class
    W = W_init
    Y = convert_labels(y, C)
    numOfPoints = X_bar.shape[1]
    check_w_after = 20
    count = 0
    while count < max_count:
        mix_id = np.random.permutation(numOfPoints)
        for i in mix_id:
            x_i = X_bar[:, i].reshape(X_bar.shape[0], 1)
            y_i = Y[:, i].reshape(C, 1)
            a_i = softmax_stable(W.T @ x_i)
            W_new = W + eta * x_i @ (y_i - a_i).T
            count += 1
            if count % check_w_after == 0:
                if np.linalg.norm(W_new - W) < 1e-4:
                    return W, count
            W = W_new
    return W, count


def pred(W, X_bar):
    A = softmax_stable(W.T @ X_bar)
    return np.argmax(A, axis=0)


def main():
    np.random.seed(112)
    df = load_csv("datasets\commodity.csv")
    X = np.concatenate((df["weight"].values.reshape(1, len(
        df["weight"].values)), df["area"].values.reshape(1, len(df["area"].values))), axis=0)
    X_bar = np.concatenate(
        (np.ones((1, X.shape[1])), X), axis=0)  # data points
    y = df["type"].values  # label
    C = y.max() + 1  # num of class
    W_init = np.random.randn(X_bar.shape[0], C)
    W, it = softmax_regression(X_bar, y, W_init, 0.01)
    print(f"W =\n {W}\n after {it} loops")
    y_pred = pred(W, X_bar)
    print(f"Accuracy: {(100*accuracy_score(y, y_pred))}%")


if __name__ == "__main__":
    main()
