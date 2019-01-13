import time
import k_means as own_k_means
import k_medoids as own_k_meadoids
import h_k_means as own_h_k_means
import import_data as toolbox_import
import numpy as np

raw = toolbox_import.convertIntoArray('Data/USCensus1990.data.txt', 69, 2, 1000)

data = np.empty(shape=(1000, 3))

data[:, 0] = raw[:, 31]
data[:, 1] = raw[:, 40]
data[:, 2] = raw[:, 12]
k = 3


def k_medoids():
    start_time = time.time()
    medoids = own_k_meadoids.initialize_k_medoids(k, data)
    cluster_assignments = own_k_meadoids.cluster(k, data, medoids)
    own_k_meadoids.improve(k, medoids, data, cluster_assignments)
    return time.time() - start_time


def k_means():
    start_time = time.time()
    own_k_means.k_means(data, k)
    return time.time() - start_time


def h_k_means():
    start_time = time.time()
    medoids = own_h_k_means.initialize_k_medoids(k, data)
    own_h_k_means.improve(k, medoids, data)
    return time.time() - start_time


number_of_loops = 50000
means_time = np.zeros(shape=number_of_loops)
medoids_time = np.zeros(shape=number_of_loops)
h_k_time = np.zeros(shape=number_of_loops)

for i in range(number_of_loops):
    means_time[i] = k_means()
    medoids_time[i] = k_medoids()
    h_k_time[i] = h_k_means()


print('K : ', k)
print('number of loops: ', number_of_loops)
print('mean time: ', np.average(means_time), 'mean std: ', np.std(means_time))
print('medoid time: ', np.average(medoids_time), 'medoid std: ', np.std(medoids_time))
print('h k time: ', np.average(h_k_time), 'h k std: ', np.std(h_k_time))
