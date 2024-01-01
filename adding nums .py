# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# note that the lists are reversed 
head = ListNode()
carry=0
curr = head
while ( l1 or l2 or carry):
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    val = val1+val2+carry
    carry = val // 10
    val = val % 10 
    curr.next = ListNode(val)
    curr =curr.next
    l1= l1.next if l1 else None
    l2 = l2.next else None
return head.next

