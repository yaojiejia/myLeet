class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path_sums = []
        if not root:
            return False   # should return bool
        
        def helper(r, s):
            if not r:
                return
            if not r.left and not r.right:   # leaf
                path_sums.append(s)
                return
            if r.left:
                helper(r.left, s + r.left.val)
            if r.right:
                helper(r.right, s + r.right.val)

        helper(root, root.val)  # start with root.val
        return targetSum in path_sums
