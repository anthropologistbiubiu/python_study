from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head:
           return head
       pre = head
       while pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
       return head
