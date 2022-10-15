k=int(input())
count=0
l=list(map(int,input().split()))
for i in range(k):
    if(l[i]==2):
        count+=1
print(count)
        
