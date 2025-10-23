# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def f(r):
            nonlocal res

            if not r:
                return 0
            left = f(r.left)
            right = f(r.right)
            res = max(res, left + right)

            return 1 + max(left,right)
        f(root)
        return res