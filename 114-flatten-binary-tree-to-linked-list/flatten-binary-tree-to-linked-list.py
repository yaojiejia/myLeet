# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        l = []
        
        def f(r):
            if not r:
                return
            l.append(r)
            f(r.left)
            f(r.right)
        f(root)
        if l:
            l.pop(0)
        while l:
            root.right = l.pop(0)
            root.left = None
            root = root.right
        
        