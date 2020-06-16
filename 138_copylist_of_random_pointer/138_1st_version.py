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
        if head==None:
            return None
        nodedict={}
        cur=head
        while cur!=None:
            nodedict[cur]=Node(cur.val)
            cur=cur.next
        tem=head
        while tem!=None:
            nodedict[tem].next=nodedict.get(tem.next)
            nodedict[tem].random=nodedict.get(tem.random)
            tem=tem.next
        return nodedict.get(head)