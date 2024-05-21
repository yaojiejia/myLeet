from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0
        
        result = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_length = len(queue)
            
            for _ in range(level_length):
                curr = queue.popleft()
                level_sum += curr.val
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            result.append(level_sum)
        
        # Find the level with the maximum sum (1-indexed)
        max_sum = max(result)
        return result.index(max_sum) + 1
