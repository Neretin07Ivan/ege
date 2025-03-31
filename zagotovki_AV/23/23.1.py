def F(n,x):
    if n==x:
        return 1
    elif n>x:
        return 0
    else:
        return F(n+1,x)+F(n*3,x)
print (F(3,33))