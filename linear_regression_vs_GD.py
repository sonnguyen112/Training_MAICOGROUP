import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


def load_csv(file_path):
    return pd.read_csv(file_path)


def gradient(w, X_bar, y):
    N = X_bar.shape[0]
    return 1/N * X_bar.T @ (X_bar @ w - y)


def is_stop(w, X_bar, y):
    return np.linalg.norm(gradient(w, X_bar, y))/len(w) < 1e-3


def GD_momentum(w_init, X_bar, y, eta, gamma):
    w = np.array(w_init)
    v_old = np.zeros_like(w_init)
    for i in range(100000):
        v_new = gamma * v_old + eta * gradient(w , X_bar, y)
        w_new = w - v_new
        if is_stop(w_new, X_bar, y):
            break
        v_old = v_new
        w = w_new
    return w_new[0, 0], w_new[1, 0], i


def linear_regression_vs_GD(input_data, real_outcome, w_init, eta, gamma=0.9):
    one_matrix = np.ones((input_data.shape[0], 1))
    X_bar = np.concatenate((one_matrix, input_data), axis=1)
    y = real_outcome
    return GD_momentum(w_init, X_bar, y, eta, gamma)


def visualize(X_test, y_test, y_pred):
    plt.plot(X_test, y_test, "bo", X_test, y_pred, "r-")
    plt.title("The plot generated from algorithm")
    plt.show()
    sns.set_theme(color_codes=True)
    df_test = pd.DataFrame({
        "Marketing": X_test,
        "Sales": y_test
    })
    sns.regplot(x="Marketing", y="Sales", data=df_test).set_title(
        "The plot generated auto from seaborn used to check")
    plt.show()


def main():
    df = load_csv("datasets/financial.csv")
    X_train, X_test, y_train, y_test = train_test_split(np.array(
        df["Marketing"]), np.array(df["Sales"]), test_size=0.2, random_state=42)
    input_data = X_train.reshape(1, len(X_train)).T
    real_outcome = y_train.reshape(1, len(y_train)).T
    w_0, w_1, i = linear_regression_vs_GD(
        input_data, real_outcome, [[2], [1]], 0.0001)
    print(f"w_0 = {w_0}, w_1 = {w_1} after {i} loop")
    y_pred = w_0 + X_test * w_1
    result = pd.DataFrame({
        "Marketing": X_test,
        "Sales Test": y_test,
        "Sales Predict": y_pred
    })
    print(result)
    visualize(X_test, y_test, y_pred)


if __name__ == "__main__":
    main()
