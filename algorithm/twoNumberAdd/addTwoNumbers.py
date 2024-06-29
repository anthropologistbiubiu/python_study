from typing import Optional



class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2:
          val1 = l1.val if l1 else 0
          val2 = l2.val if l2 else 0
          carry = (carry + val1 + val2) // 10
          val = (carry + val1 + val2) % 10
          cur.next = ListNode(val)
          cur = cur.next
          if l1:
              l1 = l1.next
          if l2:
              l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next
