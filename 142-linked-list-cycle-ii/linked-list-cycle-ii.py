class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # Check for edge cases: empty list or single node list without cycle
        if not head or not head.next:
            return None
        
        # First step: determine if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # If no cycle is detected, return None
            return None
        
        # Second step: find the entry point of the cycle
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        
        return slow
