class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

sol = Solution()
string_to_test = "moon  "
print(sol.lengthOfLastWord(string_to_test))