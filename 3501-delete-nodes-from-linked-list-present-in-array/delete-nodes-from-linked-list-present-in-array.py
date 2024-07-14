class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        count = Counter(nums)
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy

        while cur:
            if cur.val in count:
                prev.next = cur.next  # Skip the node with value in nums
            else:
                prev = cur  # Move prev to current node
            cur = cur.next  # Move to the next node

        return dummy.next