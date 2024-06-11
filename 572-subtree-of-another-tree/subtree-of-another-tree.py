class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, r, s):
        if not r and not s:
            return True
        if not r or not s or r.val != s.val:
            return False
        return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)
