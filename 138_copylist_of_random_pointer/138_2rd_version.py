"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur=head
        while cur!=None:
            tem=Node(cur.val)
            tem.next=cur.next
            cur.next=tem
            cur=cur.next.next
        cur=head
        while cur!=None:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        clone_head=head.next
        cur=clone_head
        while cur.next!=None:
            cur.next=cur.next.next
            cur=cur.next
        return clone_head
