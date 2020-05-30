# sum of two numbers by single looping structure
class solution():
      def __init__(self,ls,target):
      	  self.ls=ls
	  self.target=target

      def seqnum(self):

      	  for i in self.ls:
			tarnum=self.target-i
			if tarnum in ls:
				if tarnum==i:
					pass
				else:
					seq1=self.ls.index(i)
					seq2=self.ls.index(tarnum)
					print('sequence numbers are',seq1,seq2)
				

ls=input('Please input your number list:')
target=input('please input your target number:')
sum=solution(ls,target)
sum.seqnum() 
