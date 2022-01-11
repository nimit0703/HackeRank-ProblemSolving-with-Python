#https://www.hackerrank.com/challenges/between-two-sets/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    m1=max(a)
    m2=min(b)
    arr=set()
    arr2=set()
    c1=c2=0
    for i in range(m1,m2+1):
        for j in range(len(a)):
            if i%a[j]==0:
                c1+=1
        if c1==len(a):
            arr.add(i)
        c1=0
        for j in range(len(b)):
            if b[j]%i==0 :
                c2+=1
        if c2==len(b):
            arr2.add(i)
        c2=0
  
    arr=arr.intersection(arr2)
                
    return len(arr)               
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
