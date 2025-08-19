class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def f(p, q):
            if not p:           # if p is None, merged subtree is q
                return q
            if not q:           # if q is None, just return p
                return p

            # both p and q exist
            p.val += q.val

            # merge left children
            if not p.left:      # if p is missing left, attach q.left
                p.left = q.left
            else:               # otherwise merge deeper
                f(p.left, q.left)

            # merge right children
            if not p.right:     # if p is missing right, attach q.right
                p.right = q.right
            else:               # otherwise merge deeper
                f(p.right, q.right)

            return p

        return f(root1, root2)
