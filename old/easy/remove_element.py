from typing import List

"""Does not work because swaps too many times"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return 0
        
        num_swaps = 0
        end_pointer = len(nums)-1
        for idx, n in enumerate(nums):
            if n == val:
                while nums[end_pointer] == val and idx < end_pointer:
                    end_pointer -= 1
                    
                temp = nums[end_pointer]
                nums[end_pointer] = val
                nums[idx] = temp
                num_swaps += 1
            
        return num_swaps