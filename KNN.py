import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_txt(file_path):
    return pd.read_csv(file_path, sep="\t")


def distance(point1, point2):
    return np.linalg.norm(point2 - point1)


def most_occur_label(arr):
    label = [0, 0, 0, 0, 0]
    for x in arr:
        label[x["label"]] += 1
    return label.index(max(label[1], label[2], label[3], label[4]))


def check_null(point):
    for x in point:
        if x == None:
            return True
    return False


def KNN(X_test, X_train, y_train, K=1):
    y_pred = np.array([], dtype=int)
    for test in X_test:
        if check_null(test):
            continue
        distances = []
        for i in range(X_train.shape[0]):
            if (check_null(X_train[i])):
                continue
            distances.append({
                "label": y_train[i],
                "distance": distance(test, X_train[i])
            })
        distances_sorted = sorted(distances, key=lambda x: x["distance"])
        y_pred = np.append(y_pred, most_occur_label(distances_sorted[:K]))
    return y_pred


def main():
    df = load_txt("datasets/fruits.txt")
    X_train, X_test, y_train, y_test = train_test_split(
        np.array(df[["mass", "width", "height"]]), np.array(df["fruit_label"]), test_size=0.2, random_state=42)
    y_pred = KNN(X_test, X_train, y_train, 3)
    print(y_test)
    print(y_pred)
    print(f"Accuracy of KNN: {(100*accuracy_score(y_test, y_pred))}%")


if __name__ == "__main__":
    main()
