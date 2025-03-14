
from typing import Optional

class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 初次判断        
        if not head or not head.next:
            return True  

        fast = head
        slow = head
        # 1 -> 2
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        
        right = self.reverseLinkedList(slow)

        left = head 

        while not right and not left:
            if right.val != left.val:
                return False
        return True

    def reverseLinkedList(self,slow:Optional[ListNode]) -> Optional[ListNode]:
        pre = None 
        next_node = None 
        while slow:
            next_node = slow.next
            slow.next = pre
            pre = slow
            slow = next_node 
        return pre 
