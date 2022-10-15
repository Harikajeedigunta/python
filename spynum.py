def isspy(num):
  s=0
  p=1
  while num:
      d=num%10
      num=num//10
      s+=d
      p*=d
  return p==s
n=int(input())
res=isspy(n)
print(res)
    
