import math as M
def isperfect(num):
   res=1
   i=2
   sq=int(M.sqrt(num))
   for i in range(2,int(M.sqrt(num)):
     if(n%i==0):
       res+=i
       res+=num//i
     return res==num
t=int(input())
for _ in range(t):
  num=int(input())
  res=isperfect(num)
  print(res)
