# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a floating head infront of the two linked lists
        head = ListNode()
        print(head)

        #set the current node to that head
        curr = head

        #loop while both lists have values
        while(list1 and list2):
            
            #if the first node in list1 is smallet than list 2
            if list1.val < list2.val:

                #connect the head to list1
                curr.next = list1
                #move head of list1 down a node
                list1 = list1.next
                #move curr to the proccessed node
                curr = curr.next

            else:
                #do the same with list2
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        #any left over nodes get added in here
        curr.next = list1 or list2
        #return head.next because it is floating one before the actual list
        return head.next