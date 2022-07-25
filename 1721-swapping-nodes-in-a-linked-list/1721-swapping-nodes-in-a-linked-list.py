# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        li = []
        while cur:
            li.append(cur)
            cur = cur.next
        li[k-1].val,li[-k].val = li[-k].val,li[k-1].val
        return head
        
            