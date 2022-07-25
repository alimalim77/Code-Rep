# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        prev = temp
        cur = head
        
        if not cur.next and n:
            return None
            
        
        if not head:
            return None
        ctr  = 0
        while cur:
            ctr = ctr + 1
            cur = cur.next
        point = ctr - n
        
        
        ctr = 0
        cur = head
        while cur and ctr < point:
            ctr += 1
            temp = cur
            cur = cur.next

        #if temp and cur:
         #   temp.next = cur.next

        if temp == head:
            if cur and not cur.next:
                head.next = None
                return temp
            else:
                temp.next = cur.next 
                return head
        if temp == prev:
            if not temp.next:
                return None
            else:
                return temp.next.next
        if temp and not temp.next:
            return head
        elif temp and temp.next:
            temp.next = temp.next.next
        return head
        
                
#          [1]
# 1   [1,2]
#2
        
        
            
        
        