# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        flag = True
        cur = head
        
        temp = ListNode(0)
        ret = temp
        while cur:
            if flag:
                temp.next = ListNode(cur.val)
                temp = temp.next
                cur = cur.next
            else:
                cur = cur.next
            flag = not flag
        
        cur = head
        flag = True
        while cur:
            if flag:
                cur = cur.next
            else:
                temp.next = ListNode(cur.val)
                temp = temp.next
                cur = cur.next
            flag = not flag

        return ret.next
            
            