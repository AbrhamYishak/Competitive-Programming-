# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

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
    s = string()
    half = Counter(s)
    other_half = set()
    ans = 0
    for i in s:
        other_half.add(i)
        half[i]-=1
        if not half[i]:
            del half[i]
        ans = max(ans,len(half)+len(other_half))
    print(ans)

