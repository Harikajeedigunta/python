N,money=map(int,input().split())
count=0
i=0
while i<N:
    count+=money
    i+=2
print(count)
