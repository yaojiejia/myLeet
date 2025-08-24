class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        curr = []

        def findPath(r, target, direction):
            if not r:
                return
            curr.append([r.val, direction])
            if r.val == target:
                path.append(curr[:])
                curr.pop()
                return
            findPath(r.left, target, 'L')
            findPath(r.right, target, 'R')
            curr.pop()

        findPath(root, startValue, '')
        findPath(root, destValue, '')

        first, second = path[0], path[1]

        # 1. strip common prefix (LCA part)
        i = 0
        while i < len(first) and i < len(second) and first[i][0] == second[i][0]:
            i += 1

        # 2. From start → LCA: all "U"
        up_moves = "U" * (len(first) - i)

        # 3. From LCA → dest: directions from second[i:]
        down_moves = "".join([d for _, d in second[i:]])

        return up_moves + down_moves
