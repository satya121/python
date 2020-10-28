t=int(input())
while(t>0):
    t-=1
    tc=int(input())
    lst=[i for i in range(1,tc)]
    count=0
    while(len(lst)>0):
        a=lst[-1]//2
        lst=lst[ :a]
        count+=1
    print(count,end='')
