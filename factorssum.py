import math
i=1
num=int(input())
sq=int(math.sqrt(num))
def factors_sum(num):
    global i
    V=0
    if i>sq:
        return 0
    if num%i==0:
        if i!=num//i:#2 50 
            V=i+num//i
        else:
            V+=i
    i+=1
    return V+factors_sum(num)
print(factors_sum(num))
