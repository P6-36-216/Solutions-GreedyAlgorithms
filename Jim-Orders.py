#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders,n):
    serve=[]
    for i, j in enumerate(orders):
        serve.append([j[0]+j[1],i+1])
    serve.sort()
    lis = [i[1] for i in serve]
    return lis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
