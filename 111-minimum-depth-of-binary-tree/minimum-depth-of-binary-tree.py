# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        def helper(r, depth):
            if not r:
                return
            if not r.left and not r.right:
                res.append(depth + 1)
                return 

            helper(r.left, depth + 1)
            helper(r.right, depth + 1)

        helper(root, 0)

        return min(res)