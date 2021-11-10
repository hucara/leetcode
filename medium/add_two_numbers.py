from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        prev_node = None
        first_node = None
        while l1 or l2:
            value = 0
            value += l1.val if l1 else 0
            value += l2.val if l2 else 0 
            value += 1 if carry else 0
            
            carry = 1 if value > 9 else 0
            value = value % 10
            node = ListNode(value)
            
            if prev_node:
                prev_node.next = node
            else:
                first_node = node
            prev_node = node
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry:
            prev_node.next = ListNode(1)
            
        return first_node