# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        lp = 0
        rp = len(arr) - 1

        maxcount = 0
        while lp < rp:
            count = arr[lp] + arr[rp]
            maxcount = max(count,maxcount)
            lp += 1
            rp -= 1
        return maxcount

        
        