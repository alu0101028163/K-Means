import pytest
import functions


def test_euclid_distance():
    assert round(functions.euclid_distance([0,3,4,5],[7,6,3,-1]),3) == 9.747
    assert round(functions.euclid_distance([1,2],[3,4]),3) == 2.828
    assert round(functions.euclid_distance([1.5, 2.3],[1.5, 2.3]), 3) == 0.000
    assert round(functions.euclid_distance([1.5, 2.3],[2.3, 1.5]), 3) == 1.131
