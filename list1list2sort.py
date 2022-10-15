N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(N):
    A.sort()
    B.sort()
if(A==B):
    print(1)
else:
    print(0)
