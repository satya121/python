str1=input("enter a string")
count1,count2=0,0
def letters(n):
    global count1,count2
    for i in range(0,len(n)):
        if(n[i]<='z' and n[i]>='a'):
            count1+=1
        elif(n[i]<='Z' and n[i]>='A'):
            count2+=1
        else:
            pass
letters(str1)
print("upper case:" +str(count2))
print("lower case:" +str(count1))

