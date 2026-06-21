# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        #move the ahead pointer n+1 nodes ahead of the behind node
        for _ in range(n+1):
            ahead = ahead.next
        
        #while the ahead node is not None move both pointers down the list
        while ahead:
            behind = behind.next
            ahead = ahead.next

        #cut out targeted node
        #ends one before to move pointer to the node after the target
        behind.next = behind.next.next
        
        return dummy.next