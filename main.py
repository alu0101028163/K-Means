import functions
import loader
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

colors = ['blue','green','red','cyan','magenta','yellow','black','white']


assert(len(sys.argv) == 4)

points, dimension, size = loader.load()
k = int(sys.argv[2])
mode = sys.argv[3]

centroids, clusters = functions.k_means(k, points)

if(dimension == 3 and (mode == "-g" or mode == "--graphic")):

    centroids = np.array(centroids)

    ax = plt.axes(projection='3d')

    for key, cluster in clusters.items():
        cluster = np.array(cluster)
        centroid = centroids[int(key)]
        ax.scatter(cluster[:,0],cluster[:,1], cluster[:,2], color = colors[int(key)], marker = 'o')
        ax.scatter(centroid[0],centroid[1], centroid[2], color = colors[int(key)], marker = "s")

    plt.show()

elif(dimension == 2 and (mode == "-g" or mode == "--graphic")):

    centroids = np.array(centroids)

    ax = plt.axes(projection='3d')

    for key, cluster in clusters.items():
        cluster = np.array(cluster)
        centroid = centroids[int(key)]
        ax.scatter(cluster[:,0],cluster[:,1], color = colors[int(key)], marker = 'o')
        ax.scatter(centroid[0],centroid[1], color = colors[int(key)], marker = "s")

    plt.show()

# elif mode == '--test'
