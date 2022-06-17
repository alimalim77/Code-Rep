# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if not root:
                return 0,0,float(inf)
            left = trav(root.left)
            right = trav(root.right)
            
            dp = left[1]+right[1]
            dp1 = min(left[2]+min(right[1:]),right[2]+min(left[1:]))
            dp2 = 1 + min(left) + min(right)
            
            return dp,dp1,dp2
        
        return min(trav(root)[1:])