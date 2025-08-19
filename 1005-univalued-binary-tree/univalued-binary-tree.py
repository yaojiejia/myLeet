# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(r, val):
            if not r:
                return True
            if r.val != val:
                return False
            return helper(r.left, val) and helper(r.right, val)
        
        return helper(root, root.val)
