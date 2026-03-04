# test_lab_1d.py

import pytest
from labs.lab_1.lab_1d import two_sum

# -------------------------
# Standard test cases
# -------------------------
def test_basic_case():
    # Two numbers at the beginning
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_numbers_at_end():
    # Two numbers at the end of the list
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]

# -------------------------
# Edge cases
# -------------------------
def test_negative_numbers():
    # Includes negative numbers
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

def test_duplicate_numbers():
    # Duplicate numbers in the list
    assert two_sum([3, 3], 6) == [0, 1]

def test_large_numbers():
    # Large numbers
    assert two_sum([1000000, 500000, 500000], 1000000) == [1, 2]

def test_mixed_positive_negative():
    # Mix of positive and negative numbers
    assert two_sum([-1, -2, 4, 7], 5) == [1, 3]

# -------------------------
# Single pair at start and end
# -------------------------
def test_pair_first_and_last():
    # Pair is first and last elements
    assert two_sum([1, 3, 5, 7, 9], 10) == [1, 3]  # 3 + 7 = 10

# -------------------------
# Test coverage of all lines
# -------------------------
def test_pair_middle():
    # Pair in the middle
    assert two_sum([1, 2, 3, 4, 5], 7) == [2, 3]  # 3 + 4 = 7