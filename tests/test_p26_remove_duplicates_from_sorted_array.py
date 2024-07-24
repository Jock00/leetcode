import pytest
from src.p26_remove_duplicates_from_sorted_array import Solution

def test_sol():
    arr = [1, 1, 2]
    output = 2
    expected_output = [1, 2]

    sol = Solution()
    sol.removeDuplicates(arr)

    assert len(arr) - arr.count("_") == output

    for pos in range(0, len(expected_output)):
        assert expected_output[pos] == arr[pos]