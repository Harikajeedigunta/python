n=int(input())
d=list(map(int,input().split()))
j=0
for i in range (n):
    if(n[i]==1):
        d[i],d[j]=d[j],d[i]
        j+=1
print(*d)
