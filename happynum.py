def ishappy(num):#91
    if num<=9:
        return num==1 or num==7
    s=0
    while num:
        d=num%10
        num=num//10
        s=s+d*d
    return ishappy(s)
    
num=int(input())
res=ishappy(num)
print(res)
