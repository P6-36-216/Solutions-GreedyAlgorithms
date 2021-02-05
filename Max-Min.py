#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr,n):
    arr.sort()
    temp=[]
    for i in range(0,n-k+1):
        temp.append(arr[i+k-1]-arr[i])
    return min(temp)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
