class Solution:
    def isPalindrome(self, x: int) -> bool:
        head = 0
        x_str = str(x)
        tail = len(x_str)-1
        while head != tail and head < tail:
            if x_str[head] != x_str[tail]:
                return False
            
            head += 1
            tail -= 1
        
        return True