# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # use kadane's algorithm for trees
        # for every node, either include this node into the path sum or start a new path from this node
        # three choices, for each node, include the best path from either left, right, or both
        # 1 -> 2 
        #   -> 3
        # At 1, we can either take 1+max(left,right) or 1+left+right which is 6

        curr = root.val
        res = root.val
        
        def f(r):
            nonlocal curr
            nonlocal res
            if not r:
                return 0
            left = max(0, f(r.left))
            right = max(0, f(r.right))

            curr = r.val + max(left,right)
            res = max(res, r.val+left+right, curr)

            return curr
        f(root)
        return res