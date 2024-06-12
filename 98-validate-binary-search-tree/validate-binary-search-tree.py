# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.valid(root, float("-inf"), float("inf"))
    def valid(self, root, left, right):
        if not root:
            return True
        if not (root.val < right and root.val > left):
            return False
        return (self.valid(root.left, left, root.val) and self.valid(root.right, root.val, right))
        