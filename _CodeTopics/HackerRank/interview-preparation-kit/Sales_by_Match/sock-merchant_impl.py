#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    res = 0
    dic = {}
    for colorNum in ar:
        if not dic.has_key(colorNum):
            dic[colorNum] = 1
        else:
            dic[colorNum] += 1
    
    for value in dic.values():
        res += value / 2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
https://www.hackerrank.com/challenges/sock-merchant/submissions/code/183143233
"""
