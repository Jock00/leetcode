class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

sol = Solution()
arr = [3, 2, 4]
target = 6
print(sol.twoSum(arr, target))