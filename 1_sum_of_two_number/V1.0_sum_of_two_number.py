# sum of two numbers
class solution():
      def __init__(self,ls,target):
      	  self.ls=ls
	  self.target=target

      def seqnum(self):

      	  for i in range(len(self.ls)-1):
	      num1=self.ls[i]

	      for j in range(i+1,len(self.ls)):
	      	  num2=self.ls[j]
		  if num1+num2==self.target:
                     seqnum=[i,j]
		     print('sequence numbers are:',seqnum)


ls=input('Please input your number list:')
target=input('please input your target number:')
sum=solution(ls,target)
sum.seqnum()
