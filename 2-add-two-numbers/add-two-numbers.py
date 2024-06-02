# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 != None or l2 != None:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            temp = v1 + v2 + carry
            carry = temp // 10
            cur.next = ListNode(temp % 10)
            cur = cur.next
        
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if carry > 0:
                cur.next = ListNode(carry)
        return head.next

