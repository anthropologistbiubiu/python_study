from typing import Optional
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        lengthA  = 0
        lenghtB = 0
        head1 = headA
        head2 = headA
        while head1:
            head1 = head1.next
            lengthA += 1
        while head2:
            head2 = head2.next
            lenghtB += 1
        fast = headA if lengthA >= lenghtB else headB
        slow = headA if lengthA < lenghtB else headB
        long = lengthA if lengthA >= lenghtB else lenghtB
        short = lengthA if lengthA < lenghtB else lenghtB
        while short < long:
            fast = fast.next
            short += 1
        while fast and slow:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None

