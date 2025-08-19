class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r):
            # base case: leaf node
            if not r.left and not r.right:
                return bool(r.val)
            
            left = helper(r.left)
            right = helper(r.right)
            
            temp = -1   
            if r.val == 2:              # OR gate
                temp = bool(left) or bool(right)
            else:                       # AND gate
                temp = bool(left) and bool(right)
            
            return temp
        
        return helper(root)
