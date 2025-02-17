# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
n,k,q = arr()
temp = [0]*(200002)
for _ in range(n):
    l,r = arr()
    temp[l]+=1
    temp[r+1]-=1
for i in range(1,len(temp)):
    temp[i] = temp[i]+temp[i-1]
for i in range(len(temp)):
    if temp[i] >=k :
        temp[i] = 1
    else:
        temp[i] = 0
for i in range(1,len(temp)):
    temp[i] = temp[i]+temp[i-1]
for j in range(q):
    l,r = arr()
    print(temp[r]-temp[l-1])

