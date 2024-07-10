class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []
        nodes = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            nodes.append(root)
            inorder(root.right)

        inorder(root)
        
        # Find the two nodes that are out of order
        m1 = m2 = -1
        for i in range(len(res) - 1):
            if res[i] > res[i + 1]:
                m2 = i + 1
                if m1 == -1:
                    m1 = i
                else:
                    break

        # Swap the values of the two nodes
        nodes[m1].val, nodes[m2].val = nodes[m2].val, nodes[m1].val
