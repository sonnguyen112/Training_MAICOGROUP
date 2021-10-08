import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_csv(file_path):
    return pd.read_csv(file_path)


def split_train_test(data, test_ratio=0.2):
    np.random.seed(42)
    shuffle_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffle_indices[:test_set_size]
    train_indices = shuffle_indices[test_set_size:]
    return data.iloc[test_indices], data.iloc[train_indices]


# w = A_dagger*b = (X_bar.T*X_bar)_dagger*X_bar.T*y
def linear_regression(input_data, real_outcome):
    X = input_data.reshape(1, len(input_data)).T
    y = real_outcome.reshape(1, len(real_outcome)).T
    one_matrix = np.ones((X.shape[0], 1))
    X_bar = np.concatenate((one_matrix, X), axis=1)
    A = X_bar.T @ X_bar
    b = X_bar.T @ y
    w = np.linalg.pinv(A) @ b
    w_0 = w[0, 0]
    w_1 = w[1, 0]
    return w_0, w_1


def total_abs_err(real_outcome, outcome):
    abs_err = abs(outcome.reshape(1, len(outcome)) -
                  real_outcome.reshape(1, len(real_outcome)))
    return abs_err.sum()


def visualize(input_data, real_outcome, outcome):
    plt.plot(input_data, real_outcome, "ro", input_data, outcome, "b-")
    plt.show()


def main():
    df = load_csv("datasets/linear_regression.csv")
    test_set, train_set = split_train_test(df)
    input_data = train_set["x"].values
    real_outcome = train_set["y"].values
    w_0, w_1 = linear_regression(input_data, real_outcome)
    test_set["y_predict"] = w_0 + w_1*test_set["x"]
    print(test_set)
    print("Total Absolute Error: ", total_abs_err(
        test_set["y"].values, test_set["y_predict"].values))
    visualize(test_set["x"], test_set["y"].values,
              test_set["y_predict"].values)


if __name__ == "__main__":
    main()
