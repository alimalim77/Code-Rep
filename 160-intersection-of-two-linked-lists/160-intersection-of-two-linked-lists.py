# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# Create a pointer at first linked list and second at the second linked list
# Create a set and traverse each time to find value of skipA and skipB
# Determine skipA and skipB by using a counter
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1,ptr2 = headA,headB
        ptSet = set()
        
        
        while ptr1:
            ptSet.add(ptr1)
            ptr1 = ptr1.next
        
        count = 0
        while ptr2:
            if ptr2 in ptSet:
                return ptr2
            ptr2 = ptr2.next
            count += 1