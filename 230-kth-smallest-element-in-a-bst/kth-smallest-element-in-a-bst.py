# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        l = []
        self.helper(root, l)
        return l[k-1]
    def helper(self, root, l):
        if root is None:
            return
        self.helper(root.left, l)
        l.append(root.val)
        self.helper(root.right, l)
