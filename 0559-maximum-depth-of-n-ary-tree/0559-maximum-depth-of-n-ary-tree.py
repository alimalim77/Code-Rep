"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def helper(root,count):
            if not root:
                return
            cur = count
            for i in root.children:
                count = max(count,helper(i,cur+1))
            return count
        return helper(root,1)
                