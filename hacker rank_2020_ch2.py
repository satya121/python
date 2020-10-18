#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def bin_to_dec(str,x):
    c=0
    sum=0
    str=str[::-1]
    for i in range(x):
        if(str[i]=='1'):
            sum+=math.pow(2,c)
        c+=1
    return sum
            
def power_fun(n):
    count=1
    tmp=[0]
    while(math.sqrt(n)>count):
        p=math.pow(2,count)
        if((n%p)==0):
            tmp.append(count)
        else:
            tmp.append(0)
        count+=1
    return max(tmp)
        
def maximumPower(s):
    # Write your code here
    max_pow=[]
    x=len(s)
    for i in range(x):
        s=s[-1]+s[0:len(s)-1]
        print(s)
        sum=bin_to_dec(s,x)
        max_pow.append(power_fun(sum))
    return max(max_pow)

if __name__ == '__main__':

    s = input()
    c=0
    for i in range(len(s)):
        if(s[i]=='0'):
            c+=1
    if(c==len(s)):
        print("-1")
    else:
        result = maximumPower(s)
        print(str(result))
