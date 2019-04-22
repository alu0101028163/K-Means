import functions
import loader
import sys
import time
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

colors = ['blue','green','red','cyan','magenta','yellow','black','white']
mode = sys.argv[1]
'''
-----------------------------------------------------------------
                            TEST MODE
    Lee todas los ficheros .txt y los ejecuta con diversas k
    para obtener el rendimiento general del algoritmo.
    Ejemplo de uso: $python3 main.py --test
-----------------------------------------------------------------
'''


if (mode == '--test'):

    assert(len(sys.argv) == 2)
    allLines = []
    k_ = -1
    fileList = os.listdir("./")
    for file in fileList:
        if ".txt" in file:
            print(file)
            points, dimension, size = loader.load(file)
            k = k_ + 1

            print("%5s %5s %5s %5s %5s %10s"%("Problema","m","K","Ejecución","SSE","CPU"))
            for i in range(5):
                k += 1
                start = time.time()
                centroids, clusters = functions.k_means(k, points)
                end = time.time()
                print("%5s %4i %5i %5i %12f %5f" % (file, size, k, i, functions.SSE(centroids,clusters), (end-start)))
else:

    points, dimension, size = loader.load()
    k = int(sys.argv[3])
    centroids, clusters = functions.k_means(k, points)


    # -------------------------------------------------------------------
    #                             3D MODE
    #     Visualiza el algoritmo K-means en 3D solamente si las
    #     dimensiones de la entrada son 3.
    #     Ejemplo de uso: $python3 main.py -g nombre_fichero.txt k
    # -------------------------------------------------------------------
    #

    if(dimension == 3 and (mode == "-g" or mode == "--graphic")):
        assert(len(sys.argv) == 4)

        centroids = np.array(centroids)

        ax = plt.axes(projection='3d')

        for key, cluster in clusters.items():
            cluster = np.array(cluster)
            centroid = centroids[int(key)]

            assert(int(key) < len(colors))

            if (len(cluster) > 0):
                ax.scatter(cluster[:,0],cluster[:,1], cluster[:,2], color = colors[int(key)], marker = 'o')
            ax.scatter(centroid[0],centroid[1], centroid[2], color = colors[int(key)], marker = "s")

        plt.show()

    # -------------------------------------------------------------------
    #                             2D MODE
    #     Visualiza el algoritmo K-means en 2D solamente si las
    #     dimensiones de la entrada son 2.
    #     Ejemplo de uso: $python3 main.py k nombre_fichero.txt k
    # -------------------------------------------------------------------

    elif(dimension == 2 and (mode == "-g" or mode == "--graphic")):
        assert(len(sys.argv) == 4)
        centroids = np.array(centroids)

        ax = plt.axes(projection='3d')

        for key, cluster in clusters.items():
            cluster = np.array(cluster)
            centroid = centroids[int(key)]

            assert(int(key) < len(colors))

            if (len(cluster) > 0):
                ax.scatter(cluster[:,0],cluster[:,1], color = colors[int(key)], marker = 'o')
            ax.scatter(centroid[0],centroid[1], color = colors[int(key)], marker = "s")

        plt.show()

    elif(dimension > 3):
        print("More than 3-D spaces cannot be plotted.")
