from typing import Optional
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenghtA = 0
        lenghtB = 0
        while headA:
            headA = headA.next
            lenghtA+=1
        while headB:
            headB = headB.next
            lenghtB += 1
        pass
