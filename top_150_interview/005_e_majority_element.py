from typing import List

# using a hashmap cpu O(n) and memory O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = {}
        if len(nums) == 1:
            return nums[0]

        for idx, n in enumerate(nums):
            if n in counter:
                counter[n] += 1
                if counter[n] >= len(nums) / 2:
                    return n
            else:
                counter[n] = 1

# using sorting cpu O(nlogn) and memory O(1)
# Intuition: 
# If the elements are sorted in monotonically increasing (or decreasing) order,
# the majority element can be found at index
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]