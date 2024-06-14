# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        return self.helper(root, 0, targetSum)
    
    def helper(self, root, curr, target):
        if not root:
            return False
        if not root.left and not root.right:
            return curr + root.val == target
        return self.helper(root.left, curr + root.val, target) or self.helper(root.right, curr + root.val, target)
