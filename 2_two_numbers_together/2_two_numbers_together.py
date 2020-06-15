# leetcode No.2 two numbers together
# Definition of singly-linked list
class ListNode():
	def __init__(self,x):
		self.val=x
		self.next=None

# Solution
def addTwonumbers(self, l1: ListNode, l2: ListNode):
	# creat the head node
	dummy=p=ListNode(None)
	s=0  #carry bit
	while l1 or l2 or s:
		s=s+(l1.val if li else 0)+(l2.val if l2 else 0)
		p.next=ListNode(s%10)
		p=p.next
		s=s//10
		l1=l1.next if l1 else None
		l2=l2.next if l2 else None
	return dummy.next
	
