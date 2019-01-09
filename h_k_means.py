import random
import numpy as np
import math as m
import k_helper as kh


x1 = np.array([3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])
x2 = np.array([5, 5, 6, 4, 5, 6, 7, 5, 6, 7, 2, 2, 3, 4, 2, 3, 4, 2, 3, 4])
data = np.column_stack((x1, x2))
k = 3


def initialize_k_medoids(k, Data):
    medoids = np.empty((k, np.size(Data, 1)))
    DAta = Data
    for n in range(k):
        i = random.randrange(np.size(DAta, 1))
        for m in range(np.size(Data, 1)):
            medoids[n, m] = DAta[i, m]
        DAta = np.delete(DAta, i, 0)
    return medoids


def calculate_medoids(k, Data, medoids):
    cluster_assignments = cluster(k, Data, medoids)
    means = np.zeros(shape=(k, Data.shape[1]), dtype=object)
    numbers = np.zeros(shape=k)
    for i in range(Data.shape[0]):
        for j in range(k):
            for l in range(Data.shape[1]):
                if j == int(cluster_assignments[i]):
                    means[j, l] = means[j, l] + Data[i, l]
                    numbers[j] = numbers[j] + 1

    for i in range(k):
        for j in range(Data.shape[1]):
            means[i, j] = (means[i, j] / numbers[i])

    return means


def cluster(k, Data, medoids):
    cluster_assignments = np.empty(np.size(Data, 0))
    for i in range(np.size(Data, 0)):
        dist = np.empty(k)
        for j in range(k):
            x1 = Data[i, :]
            x2 = medoids[j]
            dist[j] = kh.euclid_distance(x1, x2)

        cluster_assignments[i] = dist.argmin()
    return cluster_assignments


def find_greatest_dist(cluster_assignments, Data, medoids):
    combined_array = np.empty(shape=(Data.shape[0], 2), dtype=object)
    greatest_dist = np.zeros(shape=(k, 2), dtype=float)
    dist = np.empty(shape=Data.shape[0])
    for i in range(len(combined_array)):
        combined_array[i] = [cluster_assignments[i], Data[i, :]]
        x1 = Data[i, :]
        currentMedoid = int(combined_array[i, 0])
        x2 = medoids[currentMedoid]
        dist[i] = kh.euclid_distance(x1, x2)

        if greatest_dist[currentMedoid, 0] <= dist[i]:
            greatest_dist[currentMedoid] = [float(dist[i]), int(i)]

    # greatest_dist[:, 0] is the distance and greatest_dist[:, 1] is the id where it came from
    return greatest_dist


def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


def cluster_cost(Data, k, medoids, cluster_assignments):
    price = np.zeros(k)
    for i in range(0, k):
        x = Data[cluster_assignments == i, :]
        for j in range(0, np.size(x, 0)):
            cost = kh.euclid_distance(x[j, :], medoids[i, :])
            price[i] += cost
    return price


def improve(k, medoids, Data):
    Data = np.array(Data)
    cluster_assignments = cluster(k, Data, medoids)
    best_price = 10 ** 23
    price = cluster_cost(Data, k, medoids, cluster_assignments)
    old_assignments = np.zeros(shape=cluster_assignments.shape)

    while np.sum(price) < best_price and old_assignments.all() != cluster_assignments.all():
        old_assigments = cluster_assignments
        print('old: ', old_assigments, 'current: ', cluster_assignments)
        print('test if: ', old_assigments.all() != cluster_assignments.all())
        # Find the greatest distance to calc new medoids
        greatest_dist = find_greatest_dist(cluster_assignments, Data, medoids)
        # Create a new data without the furthest distance points
        new_data = np.empty(shape=(Data.shape[0] - k, Data.shape[1]))
        new_data = np.delete(Data, greatest_dist[:, 1], 0)

        for i in range(k):
            current_data = np.zeros(shape=new_data.shape)
            for j in range(new_data.shape[0]):
                if cluster_assignments[j] == i:
                    current_data[j] = new_data[j]
                else:
                    current_data[j] = 0
            current_data = np.array([x for x in current_data if x.all() != 0.])

            if current_data.all() != 0:
                for l in range(len(current_data)):
                    if not (current_data[l, :] == medoids[i, :]).all():
                        temp = medoids[i, :]
                        medoids[i, :] = current_data[l, :]
                        current_data[l, :] = temp
                        cluster_assignments = cluster(k, Data, medoids)
                        best_price_prev = best_price
                        best_price = np.sum(price)
                        price = cluster_cost(Data, k, medoids, cluster_assignments)
                    if np.sum(price) > best_price:
                        temp = medoids[i, :]
                        medoids[i, :] = current_data[l, :]
                        current_data[l, :] = temp
                        price = best_price
                        best_price = best_price_prev
            print('sum price: ', np.sum(price), 'best price: ', best_price)
            print('assigments =', cluster_assignments)

    return cluster_assignments


# medoids = initialize_k_medoids(k, data)
# print('data: ', improve(k, medoids, data))
# print(cluster_assignments)
# print('shapes', data.shape, cluster_assignments.shape)
# print('medoids', medoids)
# print('Data: ', data)
