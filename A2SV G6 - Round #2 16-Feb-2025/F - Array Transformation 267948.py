# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

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
    s = arr()
    a = Counter(s)
    b = defaultdict(int)
    for i in a:
        for k in range(1,a[i]+1):
            b[k]+=1
    ans = float("inf")
    total = len(s)
    for k in b:
        ans = min(ans,total-(k*b[k]))
    print(ans)