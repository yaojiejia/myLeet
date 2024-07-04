# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l = set()
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            l.add(root.val)
            dfs(root.right)
        dfs(root)
        if len(l) < 2:
            return -1
        sorted_list = sorted(l)
        return sorted_list[1]