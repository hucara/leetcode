from typing import List


# This problem was badly written and evaluation didn't work when I tried it.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums)
        k = 0

        while p1 < p2:
            if nums[p1] == val:
                nums.pop(p1)
                nums.append('_')
                k += 1
                p2 -= 1
            else:
                p1 += 1

        print(nums)
        return k
    

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2], 2))