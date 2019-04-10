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
