import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Number of cluster
K = 4


def load_csv(file_path):
    return pd.read_csv(file_path)


def visualize(points, labels, centers):
    X_0 = points[labels == 0, :]
    X_1 = points[labels == 1, :]
    X_2 = points[labels == 2, :]
    X_3 = points[labels == 3, :]

    plt.plot(X_0[:, 0], X_0[:, 1], "ro", X_1[:, 0], X_1[:, 1], "go",
             X_2[:, 0], X_2[:, 1], "bo", X_3[:, 0], X_3[:, 1], "yo")
    plt.plot(centers[0, 0], centers[0, 1], "rs", markersize=10)
    plt.plot(centers[1, 0], centers[1, 1], "gs", markersize=10)
    plt.plot(centers[2, 0], centers[2, 1], "bs", markersize=10)
    plt.plot(centers[3, 0], centers[3, 1], "ys", markersize=10)
    plt.show()


def init_centers():
    return np.array([[30, -60], [40, -10], [20, 10], [-20, -40]])


def assign_labels(points, centers):
    distances = cdist(points, centers)
    return np.argmin(distances, axis=1)


def update_new_centers(points, num_of_clusters, labels, centers):
    new_centers = np.zeros((num_of_clusters, points.shape[1]))
    for i in range(num_of_clusters):
        points_in_a_cluster = points[labels == i, :]
        if len(points_in_a_cluster) != 0:
            new_centers[i:] = np.mean(points_in_a_cluster, axis=0)
        else:
            new_centers[i:] = centers[i:]
    return new_centers


def is_stop(new_centers, centers):
    return (set([tuple(a) for a in centers]) ==
            set([tuple(a) for a in new_centers]))


def k_means(points, num_of_clusters):
    centers = init_centers()
    i = 0
    while True:
        labels = assign_labels(points, centers)
        new_centers = update_new_centers(
            points, num_of_clusters, labels, centers)
        if is_stop(new_centers, centers):
            break
        centers = new_centers
        i += 1
    return (new_centers, labels, i)


def main():
    global K
    df = load_csv("datasets/position.csv")
    points = np.array(df)
    centers, labels, _ = k_means(points, K)
    visualize(points, labels, centers)


if __name__ == "__main__":
    main()
