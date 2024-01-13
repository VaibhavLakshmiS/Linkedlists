class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        r,l=ListNode(),ListNode()
        rtail, ltail = r,l
        while head:
            if (head.val<x):
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head= head.next
        ltail.next=r.next
        rtail.next=None
        return l.next