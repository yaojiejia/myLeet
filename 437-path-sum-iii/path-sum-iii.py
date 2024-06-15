# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        return self.helper(root,targetSum) + (self.pathSum(root.left, targetSum)
        + self.pathSum(root.right, targetSum))
    def helper(self, root, targetSum):
        if not root:
            return 0
        count = 0

        if root.val == targetSum:
            count += 1

        count += self.helper(root.left, targetSum - root.val)
        count += self.helper(root.right, targetSum - root.val)
        return count