class Solution:

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = 0
        n2 = 0

        if not nums1:
            nums1[:] = nums2
        else:
            while True:
                while n1 < len(nums1) and nums2[n2] > nums1[n1]:
                    if nums1[n1] == 0:
                        n1 -= 1
                        break
                    n1 += 1
                nums1.insert(n1+1, nums2[n2])
                n2 += 1
                n1 += 1
                if n2 >= m:
                    break

if __name__ == "__main__":
    sol = Solution()
    a = []
    b = [1,2]
    sol.merge(a, len(a), b, len(b))
    print(a)



#assest & defend
#coderpad