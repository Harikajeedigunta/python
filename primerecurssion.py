import math as M
i=2
num=int(input())
sq=int(M.sqrt(num))
def isprime(num):
    global i
    if i>sq:
        return True
    if num%i==0:
        return False
    else:
        i+=1
        return isprime(num)
print(isprime(num))
