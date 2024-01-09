def reverse(self, ListNode head, left int , right int)
dummy = ListNode(0,head)
Leftprev, curr= dummy, head
prev = None 
for i in range ( left-1)
    Leftprev, curr = curr, curr.next
prev = None 
for i in range(r-l+1)
 curr.next=prev
prev, curr = curr, tempNext

Leftprev.next.next=curr
Leftprev.next=prev
return dummy.next

