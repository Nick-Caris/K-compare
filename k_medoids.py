# ...
# Initialize: randomly select k of the n data points as the medoids
# Assignment step: Associate each data point to the closest medoid.
# Update step: For each medoid m and each data point o associated to m swap m and o and compute the total cost of the configuration
# (that is, the average dissimilarity of o to all the data points associated to m). Select the medoid o with the lowest cost of the configuration.
# ...


import k_helper as kh
import random
import numpy as np
import matplotlib.pyplot as plt

# x1 = np.array([3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])
# x2 = np.array([5,5,6,4,5,6,7,5,6,7,2,2,3,4,2,3,4,2,3,4])
# data = np.column_stack((x1, x2))
# k = 5

def initialize_k_medoids(k, Data):
    medoids = np.empty((k, np.size(Data,1)))
    DAta = Data
    for n in range(0, k):
        i = random.randrange(np.size(DAta, 1))
        for m in range (0,np.size(Data,1)):
            medoids[n, m] = DAta[i,m]
        DAta = np.delete(DAta,i,0)
    return medoids

medoids = initialize_k_medoids(k, data)


def cluster(k, Data, medoids):
    cluster_assignments = np.empty(np.size(Data,0))
    for i in range (0,np.size(Data,0)):
        dist = np.empty(k)
        for j in range(0,k):
            x1 = np.empty(np.size(Data,1))
            for l in range (0, np.size(Data,1)):
                x1[l] = Data[i,l]
            x2 = medoids[j]
            dist[j] = kh.euclid_distance(x1,x2)
        cluster_assignments[i]= dist.argmin()
    return cluster_assignments

cluster_assignments = cluster(k, data, medoids)

def cluster_cost(Data, k, medoids, cluster_assignments):
    price = np.zeros (k)
    for i in range (0, k):
        x = Data[cluster_assignments == i,:]
        for j in range(0,np.size(x,0)):
            cost = kh.euclid_distance( x[j,:],medoids[i,:])
            price[i] += cost
    return price





def improve(k,medoids,Data, cluster_assignments):
    price =  cluster_cost(Data,k,medoids,cluster_assignments)
    best_price = 10^23
    while np.sum(price) < best_price:
        for i in range (0,np.size(medoids,1)):
            for j in range (0, np.size(Data,1)):
                if not (Data[j,:]==medoids[i,:]).all():
                    temp = medoids[i,:]
                    medoids[i,:] = Data[j,:]
                    Data[j,:] = temp
                    cluster_assignments = cluster(k,Data,medoids)
                    best_price_prev = best_price
                    best_price = np.sum(price)
                    price = cluster_cost(Data,k,medoids,cluster_assignments)
                if np.sum(price) > best_price:
                    temp = medoids[i, :]
                    medoids[i, :] = Data[j, :]
                    Data[j, :] = temp
                    price = best_price
                    best_price = best_price_prev
    return medoids, Data, cluster_assignments



improve(k, medoids, data, cluster_assignments)



# plt.figure()
# for i in range(0,k):
#     plt.scatter(x1[cluster_assignments == i],x2[cluster_assignments == i])
# plt.show()
