import sys
import os
import pytest

# Add the parent directory to sys.path so that we can import list_transfer

from src.merge_sorted_array import Solution


def test_transfer_elements():
    sol = Solution()


    # Test case 1: Basic transfer
    array_1 = [1, 2, 3]
    array_2 = [2, 5, 6]
    expected_result = [1, 2, 2, 3 ,5 ,6]
    sol.merge(array_1, len(array_1), array_2, len(array_2))
    assert array_1 == expected_result



if __name__ == "__main__":
    pytest.main()
