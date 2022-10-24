# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res  = 0
        def helper(root,parent,grandparent):
            nonlocal res
            if not root:
                return 
            if grandparent and grandparent.val % 2== 0:
                res += root.val
            helper(root.left,root,parent)
            helper(root.right,root,parent)
            
            
                
        helper(root,None,None)
        return res
        