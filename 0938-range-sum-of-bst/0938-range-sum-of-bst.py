# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = [0]
        def inorder(root,s):
            if not root:
                return s
            inorder(root.left,s)
            if low <= root.val <= high:
                self.s[0] += root.val
            inorder(root.right,s)
        inorder(root,0)
        return self.s[0]
    