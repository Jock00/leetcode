
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_element = nums[0]
        i = 1
        while nums[i] != '_' and i < len(nums) - 1:
            if nums[i] == last_element:
                nums.pop(i)
                nums.append('_')
            else:
                last_element = nums[i]
                i += 1
        return len(nums) - nums.count("_")
