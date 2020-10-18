#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(0,len(arr),2):
        sum1+=arr[i]
    for i in range(1,len(arr),2):
        sum2+=arr[i]
    if(sum1==sum2):
        print(sum1+sum2)
    elif(sum1<sum2):
        print(sum1+sum1)
    else:
        print(sum2+sum2)

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)
