from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            first = ListNode(l1.val)
            l1 = l1.next
        else:
            first = ListNode(l2.val)
            l2 = l2.next

        merged = first
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    merged.next = ListNode(l1.val)
                    l1 = l1.next
                elif l2.val <= l1.val:
                    merged.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                merged.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                merged.next = ListNode(l2.val)
                l2 = l2.next

            merged = merged.next

        return first
