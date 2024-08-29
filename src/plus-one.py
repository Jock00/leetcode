class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        extra = 1
        for index in range(len(digits)-1 , -1 , -1):
            digits[index] += extra
            if digits[index] > 9:
                extra = 1
                digits[index] = 0
            else:
                extra = 0
        if extra:
            digits.insert(0, 1)
        return digits

sol = Solution()
arr = [1,2,3]
arr = sol.plusOne(arr)
print(arr)