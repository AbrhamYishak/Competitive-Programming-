# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(1,n):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
                swaps+=1
    return [swaps,a]
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    swaps, arr = countSwaps(a)
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")