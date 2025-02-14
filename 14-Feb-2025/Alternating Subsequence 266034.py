# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
t = num()
for _ in range(t):
    n = num()
    a = arr()
    i = 0
    j = 0
    max_ele = float("-inf")
    ans = 0
    while j < n:
        if a[i] > 0 and a[j] > 0:
            max_ele = max(max_ele,a[j])
        elif a[i] > 0 and a[j] < 0:
            ans+=max_ele
            max_ele = a[j]
            i = j
        elif a[i] < 0 and a[j] < 0:
            max_ele = max(max_ele,a[j])
        elif a[i] < 0 and a[j] > 0:
            ans+=max_ele
            max_ele = a[j]
            i = j
        j+=1
    if (a[i] < 0 and a[j-1] < 0) or (a[i] > 0 and a[j-1] > 0):
        ans+=max_ele
    print(ans)