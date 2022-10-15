n=int(input())
c=1
while n:
    if n%2:
        print(c)
        break
    n=n/2
    c+=1
