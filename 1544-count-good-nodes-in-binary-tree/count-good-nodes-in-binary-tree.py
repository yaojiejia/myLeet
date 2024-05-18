# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        return self.preOrder(root, root.val)
    
    def preOrder(self, root, maxVal):
        if not root:
            return 0
        if root.val >= maxVal:
            count = 1
            maxVal = root.val
        else:
            count = 0
        count += self.preOrder(root.left, maxVal)
        count += self.preOrder(root.right, maxVal)
        return count

        
