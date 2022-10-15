import math as M
def isprime(num):
    sq=int(M.sqrt(num))
    for i in range(2,sq+1):
        if(num%i==0):
            return False
    return True
    
def issemiprime(num):
    sq=int(M.sqrt(num))
    for i in range(2,sq+1):
        if(num%i==0 and isprime(i) and isprime(num//i)):
           return True
    return False
       
        
num=int(input())
res=issemiprime(num)
print(res)
