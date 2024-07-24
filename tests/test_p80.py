import pytest
from src.p80 import Solution

def test_p27():
    sol = Solution()

    # Test case 1:
    arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]

    expected_result = [1, 1, 2, 2, 3, 4, 4, 5]

    sol.removeDuplicates(arr)

    assert len(expected_result) == len(arr) - arr.count("_")

    for pos in range(0, len(expected_result)):
        assert expected_result[pos] == arr[pos]

if __name__ == "__main__":
    pytest.main()

