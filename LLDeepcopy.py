"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldtocopy={None:None}# hashmap
        curr = head
        while curr!=None:
            copy=Node(curr.val)
            oldtocopy[curr]=copy
            curr=curr.next
        curr=head
        while curr!=None:
            copy=oldtocopy[curr]
            copy.next=oldtocopy[curr.next]
            copy.random=oldtocopy[curr.random]
            curr=curr.next
        return oldtocopy[head]