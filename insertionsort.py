def insertion_sort(d,n):
    for i in range(1,n):
        temp=d[i]
        for j in range(i-1,-1,-1):
            if d[j]<temp:
                d[j+1]=temp
                break
            else:
                d[j+1]=d[j]
        else:
            d[0]=temp
n=int(input())
d=list(map(int,input().split()))
insertion_sort(d)
print(*d)
