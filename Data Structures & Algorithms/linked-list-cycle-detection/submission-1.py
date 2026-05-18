# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #set two pointers at the start of the list
        slow, fast = head, head

        #move thorugh array watching for bounds
        while fast and fast.next:

            #move the fast pointer by two
            fast = fast.next.next
            #move the slow pointer by one
            slow = slow.next

            #if pointers are equal then there is a loop
            if fast == slow:
                return True
    
        #no loop was found
        return False
    
        