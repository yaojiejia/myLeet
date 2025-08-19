# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r):
            if not r:
                return 0, True
            
            left_h, left_bal = helper(r.left)
            right_h, right_bal = helper(r.right)
            
            height = max(left_h, right_h) + 1
            balanced = (
                left_bal and 
                right_bal and 
                abs(left_h - right_h) <= 1
            )
            return height, balanced
        
        _, is_bal = helper(root)
        return is_bal
