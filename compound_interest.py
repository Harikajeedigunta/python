def compound_interest(p,r,t):
    a=p*(pow((1+r/100),t))
    compound_interest=a-p
    print(compound_interest)
p,r,t=map(int,input().split())
compound_interest(p,r,t)

