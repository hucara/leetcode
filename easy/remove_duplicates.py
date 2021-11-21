from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count_dict = {}
        repeated = 0
        for i, n in enumerate(nums[::-1]):
            if count_dict.get(n, None) == None:
                count_dict[n] = "in"
            else:
                nums.remove(n)
                repeated += 1

        return len(set(nums))
