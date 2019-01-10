import k_means as own_k_means
import k_medoids as own_k_meadoids
import h_k_means as own_h_k_means
import import_data as toolbox_import
import numpy as np
import k_helper as kh

test_data = toolbox_import.convertIntoArray('Data/test_data_unbalance.txt', 2, 1, 6500)
centroids = toolbox_import.convertIntoArray('Data/test_centroids_unbalance.txt', 2, 1, 8)
# This needs to be 9 to be equal to the calculated centroids
k = 8


def cluster(k, Data, medoids):
    cluster_assignments = np.empty(np.size(Data, 0))
    for i in range(0, np.size(Data, 0)):
        dist = np.empty(k)
        for j in range(0, k):
            x1 = np.empty(np.size(Data, 1))
            for l in range(0, np.size(Data, 1)):
                x1[l] = Data[i, l]
            x2 = medoids[j]
            dist[j] = kh.euclid_distance(x1, x2)
        cluster_assignments[i] = dist.argmin()
    return cluster_assignments


def k_means():
    return own_k_means.k_means(test_data, k)


def k_medoids():
    medoids = own_k_meadoids.initialize_k_medoids(k, test_data)
    return own_k_meadoids.cluster(k, test_data, medoids)


def h_k_means():
    medoids = own_h_k_means.initialize_k_medoids(k, test_data)
    return own_h_k_means.improve(k, medoids, test_data)


def compare_assignments(true, test):
    score = 0
    for i in range(len(true)):
        if true[i] != test[i]:
            score = score + abs(true[i] - test[i])
    return score


real_assignments = cluster(k, test_data, centroids)


number_of_loops = 5000
means_score = np.zeros(shape=number_of_loops)
medoids_score = np.zeros(shape=number_of_loops)
h_k_score = np.zeros(shape=number_of_loops)

for i in range(number_of_loops):
    means_score[i] = compare_assignments(real_assignments, cluster(k, test_data, k_means()))
    medoids_score[i] = compare_assignments(real_assignments, k_medoids())
    h_k_score[i] = compare_assignments(real_assignments, h_k_means())


print('number of loops: ', number_of_loops)
print('mean score: ', np.average(means_score), 'mean std: ', np.std(means_score))
print('medoid score: ', np.average(medoids_score), 'medoid std: ', np.std(medoids_score))
print('h k score: ', np.average(h_k_score), 'h k std: ', np.std(h_k_score))
