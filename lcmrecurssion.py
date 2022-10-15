t=2
def lcm(a,b):
    global t
    res=1
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        res=t
    else:
        t+=1
    return res*lcm(a,b)
a,b=map(int,input().split())
print(lcm(a,b))
    
