import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_mixed_values():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_all_positive():
    assert max_subarray_sum([1,2,3,4]) == 10


def test_all_negative():
    assert max_subarray_sum([-1,-2,-3]) == -1


def test_single_element():
    assert max_subarray_sum([5]) == 5


def test_empty_list():
    with pytest.raises(ValueError):
        max_subarray_sum([])

       # Additional tests to cover remaining lines
def test_two_elements_positive_negative():
    # Covers lines 38, 42-44
    assert max_subarray_sum([1, -2]) == 1

def test_negative_followed_by_positive():
    # Covers updating max_global in loop
    assert max_subarray_sum([-100, 1, 2, 3]) == 6

def test_all_zeros():
    # Covers branch where max_current == max_global
    assert max_subarray_sum([0,0,0,0]) == 0