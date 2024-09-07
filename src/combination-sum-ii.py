class Solution:
    def combinationSum2(self,candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include the current number and move to the next
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  # Sort the candidates to handle duplicates
        print(candidates)
        result = []
        backtrack(0, target, [])
        return result


candidates = [5, 3, 1, 7]
target = 6
sol = Solution()
print(sol.combinationSum2(candidates, target))
