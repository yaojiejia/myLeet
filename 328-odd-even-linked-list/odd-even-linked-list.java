/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode eH = null;
        ListNode eT = null;
        ListNode oH = null;
        ListNode oT = null;
        ListNode current = head;
        boolean isOdd = true;
        while(current != null){
            if(isOdd){
                if(oH == null){
                    oH = current;
                    oT = current;
                }else{
                    oT.next = current;
                    oT = oT.next;
                }
            }
            else{
                if(eH == null){
                    eH = current;
                    eT = current;
                }else{
                    eT.next = current;
                    eT = eT.next;
                }
            }

            isOdd = !isOdd;
            current = current.next;
        }


        if(oT != null){
            oT.next = eH;
        }
        if(eT!=null){
            eT.next = null;
        }

        return oH;
    }
}