# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
n,k = arr()
a = arr()
d = Counter()
start = 0
max_len = 0
ans = [0,0]
for end in range(n):
    d[a[end]]+=1
    if len(d) > k:
        d[a[start]]-=1
        if not d[a[start]]:
            del d[a[start]]
        start+=1
    if end-start+1 > max_len:
        max_len = end-start+1
        ans[0] = start+1
        ans[1] = end+1
print(*ans)