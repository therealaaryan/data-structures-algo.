# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        p1 = head
        p2 = prev
        
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        
        
        
        
        
        
        