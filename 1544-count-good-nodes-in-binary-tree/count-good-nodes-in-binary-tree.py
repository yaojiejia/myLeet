# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        blue = 0  

        def good(root, parent_val):
            nonlocal blue  
            if not root:
                return
            
            if root.val >= parent_val:
                blue += 1
                good(root.left, root.val)
                good(root.right, root.val)
            else:
                good(root.left, parent_val)
                good(root.right, parent_val)
            
            return blue
        
        return good(root, root.val)