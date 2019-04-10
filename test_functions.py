import pytest
import functions
import numpy as np      # Arrays for high performance operations



def test_euclid_distance():
    assert round(functions.euclid_distance([0,3,4,5],[7,6,3,-1]),3) == 9.747
    assert round(functions.euclid_distance([1,2],[3,4]),3) == 2.828
    assert round(functions.euclid_distance([1.5, 2.3],[1.5, 2.3]), 3) == 0.000
    assert round(functions.euclid_distance([1.5, 2.3],[2.3, 1.5]), 3) == 1.131

def test_recalculate_centroid():
    cluster_a = [[1,1],[2,4]]
    cluster_b = [[1,2,3],[4,5,6],[8,9,10]]
    cluster_c = [[-2,4,5,-8],[1,-2,-2,4]]
    assert(np.array_equal(functions.recalculate_centroid(cluster_a), [1.5, 2.5]))
    assert(np.array_equal(functions.recalculate_centroid(cluster_b), [4.3,5.3,6.3]))
    assert(np.array_equal(functions.recalculate_centroid(cluster_c), [-0.5,1,1.5,-2]))
