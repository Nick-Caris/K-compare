import import_data as toolbox_import
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

raw = toolbox_import.convertIntoArray('Data/USCensus1990.data.txt', 69, 2, 10000)


data = np.empty(shape=(10000, 3))

data[:, 0] = raw[:, 31]
data[:, 1] = raw[:, 40]
data[:, 2] = raw[:, 12]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]


ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('workstate')
ax.set_ylabel('means of transport')
ax.set_zlabel('number of children')

plt.show()

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

ax.scatter(x, y, z, c=kmeans.labels_, cmap='rainbow', marker='o')

ax.set_xlabel('workstate')
ax.set_ylabel('means of transport')
ax.set_zlabel('number of children')

plt.show()
