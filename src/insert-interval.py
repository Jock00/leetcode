class Solution:
    def binary_search(self, intervals, val, left, right) -> int:

        if left > right:
            return left
        middle = (left + right) // 2
        if val > intervals[middle][0]:
            return self.binary_search(intervals, val, middle + 1, right)
        else:
            return self.binary_search(intervals, val, left, middle - 1)

    def insert(self, intervals: list[list[int]], newInterval: list[int]):
        try:
            index_to_insert = self.binary_search(intervals, newInterval[0], 0, len(intervals))
        except IndexError:
            index_to_insert = len(intervals)
        intervals.insert(index_to_insert, newInterval)

        current_index = 0
        while current_index < len(intervals) - 1:
            if intervals[current_index][1] >= intervals[current_index + 1][0] :
                elem = intervals.pop(current_index)
                intervals[current_index][0] = min(intervals[current_index][0], elem[0])
                intervals[current_index][1] = max(intervals[current_index][1], elem[1])
            else:
                current_index += 1
        return intervals


sol = Solution()
intervals = [
    [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
]

wanted_interval = [-1, 20]
# print(sol.binary_search(numbers, wanted_n, 0 , len(numbers) -1))
s = sol.insert(intervals, wanted_interval)
print(intervals)
