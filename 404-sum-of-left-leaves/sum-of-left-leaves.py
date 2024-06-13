# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        l = [0]
        self.helper(root, l, None)
        return l[0]
    def helper(self, root, l, isLeft):
        if not root:
            return 
        if root.left is None and root.right is None and isLeft:
            l[0] += root.val
        self.helper(root.left, l, True)
        self.helper(root.right, l, False)
        