class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        
        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        # Create the new linked list from the nodes in the stack
        dummy = ListNode(0)
        current = dummy
        
        for node in stack:
            current.next = ListNode(node.val)
            current = current.next
        
        return dummy.next