from collections import deque
from typing import Optional, Tuple, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize maps to store the max value when a node is robbed or not robbed
        rob = {}
        not_rob = {}

        # Use a deque for BFS
        q = deque([root])
        
        # Reverse level order to process nodes from bottom to top
        nodes = []
        while q:
            node = q.popleft()
            nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # Process nodes in reverse order
        while nodes:
            node = nodes.pop()
            left_rob = rob.get(node.left, 0)
            left_not_rob = not_rob.get(node.left, 0)
            right_rob = rob.get(node.right, 0)
            right_not_rob = not_rob.get(node.right, 0)
            
            # If we rob this node
            rob[node] = node.val + left_not_rob + right_not_rob
            # If we do not rob this node
            not_rob[node] = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

        return max(rob[root], not_rob[root])
