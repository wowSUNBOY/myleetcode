# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tem=head
        count=0
        while tem!=None:
            count=count+1
            tem=tem.next
        target=count-n+1
        print(target,count)
        if target>1:
            cur=head
            for j in range(target-2):
                cur=cur.next
            p=cur.next
            cur.next=p.next
            return head
        elif count==1:
            return None
        else:
            cur=head
            head=cur.next
            return head