"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])

        while q:
            ptr = Node()
            for i in range(len(q)):
                temp = q.popleft()
                if i == len(q) - 1:
                    temp.next = None
                ptr.next = temp
                ptr = temp
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return root