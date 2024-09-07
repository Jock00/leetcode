def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        import math
        # Create a list of numbers to get the digits from.
        numbers = list(range(1, n + 1))

        # Adjust k to be zero-indexed
        k -= 1

        # Resultant permutation sequence
        permutation = []

        # Precompute the factorials
        factorial = math.factorial(n - 1)

        for i in range(n - 1, -1, -1):
            # Determine the index of the next number to add
            index = k // factorial
            permutation.append(str(numbers[index]))

            # Remove used number from the list
            numbers.pop(index)

            # Update k and the factorial for the next iteration
            if i != 0:
                k %= factorial
                factorial //= i

        return ''.join(permutation)

#
# class Solution:
#     def factorial(n):
#         if n <= 1:
#             return 1
#         else:
#             return n * factorial(n - 1)
#
#     def getPermutation(self, n, k):
#
#         arr = [str(i) for i in range(1, n + 1)]
#         if k == 1:
#             return "".join(arr)
#         if k > factorial(len(arr) - 1):
#             k =
#         final = []
#         while arr:
#             fact = factorial(len(arr) - 1)
#             pos = k // fact
#             print(pos)
#             final.append(arr.pop(pos))
#             while k >= fact:
#                 k -= fact
#             if k <= 1:
#                 final.extend(arr)
#                 break
#         return "".join(final)
#

n = 2
k = 2

sol = Solution()
my_result = sol.getPermutation(n, k)
# print(f"Expected result: {good_result}")
print(f"Got result: {my_result}")
