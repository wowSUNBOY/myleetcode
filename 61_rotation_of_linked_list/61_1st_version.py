# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        cur=head
        len=0
        while cur is not None:
            cur=cur.next
            len=len+1
        if len==0:    # avoid empty sets
            return None
        n=k%len
        if n==0:
            return head
        else:
            pos=len-n
            tem,con=head,head
            for i in range(pos-1):
                tem=tem.next  # the first node need move
            for i in range(len-1):
                con=con.next    # the last node
            con.next=head
            head=tem.next
            tem.next=None
            return head