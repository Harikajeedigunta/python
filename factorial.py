#method 1
def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
 
# Driver Code
num = int(input())
print("Factorial of",num,"is",factorial(num))


# method 2
n=int(input())
factorial=1
if(n<0):
    print("does not exist")
if(n==0):
    print("n is 1")
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
    
