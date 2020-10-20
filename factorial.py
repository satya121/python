a=int(input("enter a number"))
def fact(n):
    if(n==0):
        result=1
    else:
        result=n*fact(n-1)
    return result

res=fact(a)
print(res)
