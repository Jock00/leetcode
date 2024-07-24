import pytest
from src.p27_remove_element import Solution

def test_p27():
    sol = Solution()

    # Test case 1:
    lst = [0, 1, 2, 2, 3, 0, 4, 2]
    v = 2

    expected_result = [0, 1, 3, 0, 4]

    sol.removeElement(lst, v)

    assert len(expected_result) == len(lst) - lst.count("_")

    for pos in range(0, len(expected_result)):
        assert expected_result[pos] == lst[pos]

if __name__ == "__main__":
    pytest.main()

