# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(r, low, high):
            if not r:
                return True
            if not (low < r.val < high):
                return False

            left  = helper(r.left, low, r.val)
            right = helper(r.right, r.val, high)

            return left and right

        return helper(root, float("-inf"), float("inf"))
