# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
      #add each node to a set
        seen = set()

        #start at the front of the list
        curr = head

        while curr:
            #if we have visited this node before there is a loop
            if curr in seen:
                return True

            #if not add the node to the set
            seen.add(curr)
            #move to the next node
            curr = curr.next

        #no loops were found
        return False
    
        