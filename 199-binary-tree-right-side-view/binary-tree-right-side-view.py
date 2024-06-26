class Solution:
    def rightSideView(self, root):
        l1 = []
        self.bfs(root, l1, 0)
        return l1

    def bfs(self, root, l, depth):
        if not root:
            return

        if depth == len(l):
            l.append(root.val)
            
        self.bfs(root.right, l, depth + 1)
        self.bfs(root.left, l, depth + 1)
