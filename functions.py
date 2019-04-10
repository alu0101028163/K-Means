import math             # For using sqrt
import numpy as np      # Arrays for high performance operations

def euclid_distance(point_a, point_b):
    if(len(point_a) != len(point_b)):
        raise Exception("Both points must have the same size when calculating Euclid Distance")
    summation = 0
    for coordinate_a, coordinate_b in zip(point_a, point_b):
        summation += pow(coordinate_a - coordinate_b , 2)
    return math.sqrt(summation)

def recalculate_centroid(points):
    summation = np.zeros(len(points[0]))
    for point in points:
        summation = np.add(summation, point)
    return np.round((summation / len(points)), 1)

# It calculates the range of each coordinate in the space.
def calculate_range(entries):
    min_range = np.copy(entries[0])
    max_range = np.copy(entries[0])
    for entry in entries:
        for i in range(len(entry)):
            if(entry[i] < min_range[i]):
                min_range[i] = entry[i]
            if(entry[i] > max_range[i]):
                max_range[i] = entry[i]

    return min_range,max_range
