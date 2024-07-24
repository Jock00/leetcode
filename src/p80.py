class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_count = 1
        current_elem = nums[0]
        pos = 1
        while pos < len(nums) - 1 and nums[pos] != '_':
            if nums[pos] == current_elem:
                if current_count >= 2:
                    nums.pop(pos)
                    nums.append('_')
                else:
                    current_count += 1
                    pos += 1
            else:
                current_elem = nums[pos]
                current_count = 1
                pos += 1
        return len(nums) - nums.count('_')
