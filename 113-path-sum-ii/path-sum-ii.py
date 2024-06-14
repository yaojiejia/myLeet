# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        self.helper(root, res, [], targetSum)
        return res
    
    def helper(self, root, res, path, target):
        if not root:
            return False
        path.append(root.val)
        if not root.left and not root.right and sum(path) == target:
            res.append(list(path))
        if root.left:
            self.helper(root.left, res, path, target)
        if root.right:
            self.helper(root.right, res, path, target)
        path.pop()
        
        