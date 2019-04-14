import math             # For using sqrt
import numpy as np      # Arrays for high performance operations
import loader
import random

def euclid_distance(point_a, point_b):
    if(len(point_a) != len(point_b)):
        raise Exception("Both points must have the same size when calculating Euclid Distance")
    summation = 0
    for coordinate_a, coordinate_b in zip(point_a, point_b):
        summation += pow(coordinate_a - coordinate_b , 2)
    return np.round(math.sqrt(summation),1)

# Esta función está petando en la primera línea.
def recalculate_centroid(points, centroid):
    if(len(points) > 0):
        summation = np.zeros(len(points[0]))
        for point in points:
            summation = np.add(summation, point)
        return np.round((summation / len(points)), 1)
    else:
        return centroid


# It calculates the range of each coordinate in the space.
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


def calculate_initial_centroids(k_means, entries):
    min_range, max_range = calculate_range(entries)
    centroids = []
    for i in range(k_means):
        centroid = []
        for min,max in zip(min_range, max_range):
             centroid.append(random.randint(int(min), int(max)))
        centroids.append(centroid)
    return centroids


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


def SSE(centroids, clusters):
    total_sum = 0
    for i in range(len(clusters)):
        cluster_sum = 0
        for point in clusters[str(i)]:
            cluster_sum += pow(euclid_distance(centroids[i], point),2)
        total_sum += cluster_sum
    return total_sum
