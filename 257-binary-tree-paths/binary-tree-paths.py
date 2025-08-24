from typing import List, Optional

# class TreeNode: ...

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res: List[str] = []
        curr: list[int] = []

        def f(r: Optional[TreeNode]) -> None:
            if not r:
                return
            curr.append(r.val)

            if not r.left and not r.right:
                res.append("->".join(map(str, curr)))  # build the path string
                curr.pop()                              # backtrack before returning
                return

            f(r.left)
            f(r.right)
            curr.pop()  # backtrack after exploring children

        f(root)
        return res
