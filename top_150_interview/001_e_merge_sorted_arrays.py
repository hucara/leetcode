from typing import List

# Dirty approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if nums2 is empty, nothing to merge
        if n == 0:
            return

        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()

# Three pointer approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # Initialize pointers 
        A, B, C = m - 1, n - 1, m + n - 1 

        # Merge from the end
        while B >= 0:
            if A >= 0 and nums1[A] > nums2[B]:
                nums1[C] = nums1[A]
                A -= 1
            else:
                nums1[C] = nums2[B]
                B -= 1
            C -= 1