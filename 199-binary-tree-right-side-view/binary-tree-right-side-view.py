# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def f(r, h):
            if not r:
                return
            if h == len(ans):
                ans.append(r.val)
            f(r.right, h+1)
            f(r.left, h+1)
        f(root, 0)
        return ans
            