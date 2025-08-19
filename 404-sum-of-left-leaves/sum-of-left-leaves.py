# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(r):
            if not r:
                return 0
            
            total = 0
            # if r.left is a leaf, add its value
            if r.left and not r.left.left and not r.left.right:
                total += r.left.val
            # otherwise, recurse
            total += helper(r.left)
            total += helper(r.right)
            return total
        
        return helper(root)
