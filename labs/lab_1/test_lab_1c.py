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