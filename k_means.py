from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import import_data as toolbox_import
from sklearn.cluster import KMeans
import math as m


# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


def k_means(dataa, k=3):
    X = np.array(dataa)
    C_dimensions = np.empty((k, X.shape[1]), dtype=np.float32)

    # coordinates of random centriods
    for i in range(k):
        random_cluster = np.random.randint(0, np.max(X), size=X.shape[1])
        C_dimensions[i] = random_cluster

    C = np.array(list(C_dimensions), dtype=np.float32)

    # To store the value of centroids when it updates
    C_old = np.zeros(C.shape)
    # Cluster Lables(0, 1, 2)
    clusters = np.zeros(len(X))
    # Error func. - Distance between new centroids and old centroids
    error = dist(C, C_old, None)
    # Loop will run till the error becomes zero
    while error != 0:
        # Assigning each value to its closest cluster
        for i in range(len(X)):
            distances = dist(X[i], C)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        # Storing the old centroid values
        C_old = deepcopy(C)
        # Finding the new centroids by taking the average value
        for i in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            if points:
                C[i] = np.mean(points, axis=0)
            else:
                C[i] = C[i]
        error = dist(C, C_old, None)
        # print(C, ' old', C_old)
        # print('Error', error)
    return C


# raw = toolbox_import.convertIntoArray('Data/USCensus1990.data.txt', 69, 2, 100)
#
# data = np.empty(shape=(100, 3))
#
# data[:, 0] = raw[:, 31]
# data[:, 1] = raw[:, 40]
# data[:, 2] = raw[:, 12]
#
# print('Eigen cluster', k_means(data, 3))
#
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(data)
#
# print('Echte cluster', kmeans.cluster_centers_)
