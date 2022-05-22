# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.cont = []
        flag = False
        def helper(root,s):
            if root == None:
                return
            print(s)
            if root.left == None and root.right == None:
                self.cont.append(s+"->"+str(root.val))
            
                
                
            helper(root.left,s+"->"+str(root.val)) if s != "" else helper(root.left,s+str(root.val))
            helper(root.right,s+"->"+str(root.val))  if s != "" else helper(root.right,s+str(root.val))
        helper(root,"")
        for idx,i in enumerate(self.cont):
            if i[:2] == "->":
                self.cont[idx] = self.cont[idx][2:]
        return self.cont
    