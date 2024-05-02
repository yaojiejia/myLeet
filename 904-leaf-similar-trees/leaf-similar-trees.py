class Solution(object):
    def leafSimilar(self, root1, root2):
        l1 = []
        l2 = []
        self.getLeaf(root1, l1)
        self.getLeaf(root2, l2)
        return l1 == l2
    
    def getLeaf(self, root, l):
        if root is None:
            return
        if root.left is None and root.right is None:
            l.append(root.val)
        else:
            self.getLeaf(root.left, l)
            self.getLeaf(root.right, l)