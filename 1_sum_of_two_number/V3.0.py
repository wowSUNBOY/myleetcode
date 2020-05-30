# sum of two numbers by dictionary
class solution():
      def __init__(self,ls,target):
            self.ls=ls
            self.target=target
		
      def seqnum(self):
        lookup={}
        for i in range(len(self.ls)):
            num=float(self.ls[i])
            tarnum=target-num
            if tarnum in lookup:
                print('sequence numbers are',i,lookup[tarnum])
            lookup[num]=i				
				

ls=input('Please input your number list:').split(" ")    # split the input str by ','
target=float(input('please input your target number:'))
sum=solution(ls,target)
sum.seqnum() 
