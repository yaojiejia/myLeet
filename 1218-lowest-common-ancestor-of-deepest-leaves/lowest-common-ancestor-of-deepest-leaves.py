# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        leaves = []
        max_depth = 0

        def findLeaves(r, d):
            nonlocal max_depth
            if not r:
                return 
            if not r.left and not r.right:
                if d >= max_depth:
                    leaves.append([r, d])  # ✅ store node, not value
                    max_depth = d
                return
            findLeaves(r.left, d + 1)
            findLeaves(r.right, d + 1)

        findLeaves(root, 0)

        # collect deepest leaves only
        target = [node for node, depth in leaves if depth == max_depth]

        def lca(r, p, q):
            if not r:
                return None
            if r is p or r is q:
                return r
            left = lca(r.left, p, q)
            right = lca(r.right, p, q)
            if left and right:
                return r
            return left if left else right

        ans = target[0]
        for i in range(1, len(target)):
            ans = lca(root, ans, target[i])

        return ans
