
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while nums[i] != '_' and i < len(nums) - 1:
            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
            else:
                i += 1
        return len(nums) - nums.count("_")

if __name__ == "__main__":
    sol = Solution()
    lst = [0,1,2,2,3,0,4,2]
    v = 2
    sol.removeElement(lst, v)
    print(lst)