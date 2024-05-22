# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        res = []

        while queue:
            level_len = len(queue)
            levelval = []
            for i in range(level_len):
                curr = queue.popleft()
                if curr:
                    levelval.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(levelval)
        return res    


        