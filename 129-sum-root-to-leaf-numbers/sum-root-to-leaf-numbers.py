# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_sums = []
        if not root:
            return []
        def helper(r, s):
            if not r:
                return
            if not r.left and not r.right:
                path_sums.append(s)
                return
            
            if r.left:
                helper(r.left, s+str(r.left.val))
            if r.right:
                helper(r.right, s+str(r.right.val))
        
        helper(root, str(root.val))
        result = 0

        for s in path_sums:
            result += int(s)
        return result
