lass Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
     
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # Check if it's a start of duplicates sequence.
            if head.next and head.val == head.next.val:
                # Skip the duplicates.
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  # Remove duplicates.
            else:
                prev = prev.next  # Move prev pointer.
            
            head = head.next  # Move head pointer.

        return dummy.next