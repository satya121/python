def celsius(x):
    c=((x*(9/5))+32)
    return(c)
celsius_list=[]
a=int(input("enter no.of elements in list"))
for i in range(0,a):
    b=int(input())
    celsius_list.append(b)
r=map(celsius,celsius_list)
print(list(r))
