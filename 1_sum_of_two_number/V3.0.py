# sum of two numbers by dictionary
class solution():
      def __init__(self,ls,target):
			self.ls=ls
			self.target=target
		
      def seqnum(self):
		lookup={}
		for i in range(len(self.ls)):
			tarnum=target-self.ls[i]
			if tarnum in lookup:
				print('sequence numbers are',i,lookup[tarnum])
			lookup[self.ls[i]]=i				
				

ls=input('Please input your number list:')
target=input('please input your target number:')
sum=solution(ls,target)
sum.seqnum() 
