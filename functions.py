import math             # For using sqrt
import numpy as np      # Arrays for high performance operations
import random

'''
Calculo de la distancia euclídea.

Lo primero que se hace es comprobar que ambos puntos comparten la misma
dimension, y a continuación se realiza un sumatorio de las diferencias de
cada coordenada al cuadrado. Lo que se retorna es la raíz de dicho sumatorio.
'''

def euclid_distance(point_a, point_b):
    if(len(point_a) != len(point_b)):
        raise Exception("Both points must have the same dimension when calculating Euclid Distance")
    summation = 0
    for coordinate_a, coordinate_b in zip(point_a, point_b):
        summation += pow(coordinate_a - coordinate_b , 2)
    return np.round(math.sqrt(summation),1)

'''
Recalcular los centroides.

Los puntos que se pasan corresponden a un clúster, por lo tanto,
lo primero que se hace es asegurarse de que hay puntos en el clúster, de otro
modo no se recalcula ningún centroide.
A continuación se realiza un sumatorio de todos los puntos y se devuelve
el cociente de este sumatorio con el total de puntos. (Una media)
'''
def recalculate_centroid(points, centroid):
    if(len(points) > 0): # Hay puntos en el clúster.
        summation = np.zeros(len(points[0]))
        for point in points:
            summation = np.add(summation, point)
        return np.round((summation / len(points)), 1)
    else:
        return centroid


'''
Esta función se encarga de buscar cuál es el valor mínimo y
máximo para cada variable de entrada. En el caso del máximo redondea
hacia el mayor valor y en el caso del mínimo lo contrario.
'''
def calculate_range(entries):
    min_range = np.copy(entries[0])
    max_range = np.copy(entries[0])
    for entry in entries:
        for i in range(len(entry)):
            if(entry[i] <= min_range[i]):
                min_range[i] = math.floor(entry[i])
            if(entry[i] >= max_range[i]):
                max_range[i] = math.ceil(entry[i])

    return min_range,max_range

'''
Calculo de los centroides iniciales.

Lo primero que hace es obtener el rango de valores posibles para
cada variable utilizando la función "calculate_range".
Posteriormente se generan valores aleatorios dentro de dicho rango
para cada una de las variables que conformarán un centroide.
Esto se repite tantas veces como el número de k sea especificado.
Los centroides se almacenan en una lista que es retornada.
'''
def calculate_initial_centroids(k_means, entries):
    min_range, max_range = calculate_range(entries)
    centroids = []
    for i in range(k_means):
        centroid = []
        for min,max in zip(min_range, max_range):
             centroid.append(random.randint(int(min), int(max)))
        centroids.append(centroid)
    return centroids

'''
Calculo de los clústers.

Los clústers se almacenan en un diccionario que tiene la
apariencia:

clusters = {
    '0': [[...],[...][...]],
    '1': [[...],[...][...]]
  '...': [[...],[...],...]
}

Donde la clave es el índice que corresponde a cada centroide
y el valor es una lista de listas que representan los puntos de cada clúster.

A la función se la pasa por parámetro los centroides y puntos.

Lo primero que se hace es inicializar el dicionario.
A continuación se calcula para cada punto el centroide con el que
comparte la menor distancia y dicha distancia.
Al centroide en cuestión que minimice la distancia se le asignará
dicho punto en el diccionario.
Se retorna el diccionario con el índice del centroide y sus correspondientes
puntos. (Clústers)
'''
def calculate_clusters(centroids, points):
    # Initialize map containing the points for each centroid
    clusters = {}
    for i in range(len(centroids)):
        clusters[str(i)] = []

    for point in points:
        minDistance = euclid_distance(point,centroids[0])
        minCentroid = 0
        for i in range(len(centroids)):
            if (minDistance > euclid_distance(point,centroids[i])):
                minDistance = euclid_distance(point,centroids[i])
                minCentroid = i
        clusters[str(minCentroid)].append(point)

    return clusters


'''
Algoritmo K-Means.

Esta función pone en marcha muchas de las funciones previamente descritas.
Una vez se calculan los centroides iniciales lo que se hace es que iterar
mientras la variable booleana change sea verdadera.
En el cuerpo de dicho bucle primero se calculan los clústers, a continuacion se
recalculan los centroides comparandose cada nuevo centroide con el previo,
si existe alguna diferencia ha habido un cambio.
Cuando no hay cambios se ha llegado al final del algoritmo y por lo tanto
se retornan los centroides y clústers.
'''
def k_means(k, points):

    centroids = calculate_initial_centroids(k, points)
    clusters = []
    change = True
    while(change):
        clusters = calculate_clusters(centroids, points)
        for i in range(len(centroids)):
            new_centroid = recalculate_centroid(clusters[str(i)], centroids[i])
            change = False
            for point_new, point_old in zip(new_centroid, centroids[i]):
                if (point_new != point_old):
                    change = True
            centroids[i] = new_centroid

    return centroids, clusters


'''
Calculo de la suma de errores al cuadrado.

Se realiza un sumatorio de las distancias eucledianas al cuadrado
de cada centroide a sus puntos dentro de cada clúster.
Todos estos sumatorios en cada clúster son sumados a su vez y retornados.
'''
def SSE(centroids, clusters):
    total_sum = 0
    for i in range(len(clusters)):
        cluster_sum = 0
        for point in clusters[str(i)]:
            cluster_sum += pow(euclid_distance(centroids[i], point),2)
        total_sum += cluster_sum
    return total_sum
