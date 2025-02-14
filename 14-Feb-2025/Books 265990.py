# Problem: Books - https://codeforces.com/contest/279/problem/B

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
n,t = arr()
book = arr()
start = 0
ans = 0
for end in range(n):
    t-=book[end]
    while t < 0:
        t+=book[start]
        start+=1
    ans=max(ans,end-start+1)
print(ans)