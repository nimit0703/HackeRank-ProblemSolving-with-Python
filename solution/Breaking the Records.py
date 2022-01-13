#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    ma=mi=scores[0]
    c1=c2=0
    c=list()
    for i in scores[1:]:
        if i>ma:
            ma=i
            c1 += 1
        if i<mi:
            mi=i
            c2 +=1
    c.append(c1)
    c.append(c2)
    return c
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
