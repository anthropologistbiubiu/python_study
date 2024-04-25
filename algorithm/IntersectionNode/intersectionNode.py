from typing import Optional
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA  = 0
        lenghtB = 0
        while headA:
            headA = headA.next
            lengthA += 1
        while headB:
            headB = headB.next
            lenghtB += 1
        fast = headA if lengthA > lenghtB else headB
        slow = headA if lengthA < lenghtB else headB
        long = lengthA if lengthA > lenghtB else lenghtB
        short = lengthA if lengthA < lenghtB else lenghtB
        while short < long:
            fast = fast.next
            short += 1
