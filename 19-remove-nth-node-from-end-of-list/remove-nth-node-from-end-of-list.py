class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        current = head
        while(current != None):
            count += 1
            current = current.next
        num = count - n
        current = head
        counter = 0
        if num == 0:
            return head.next
        while(current.next != None):
            counter += 1
            if counter == num:
                current.next = current.next.next
                break
            current = current.next
        return head
