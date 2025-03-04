# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

###########--------Template-----------#########
from math import *
from collections import *
from random import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
def randomnum(): return randint(0,1)
###########--------Template-----------#########
n = num()
v = arr()
unsorted = [0,v[0]]
for i in range(1,len(v)):
    unsorted.append(unsorted[-1]+v[i])
v.sort()
sorted = [0,v[0]]
for i in range(1,len(v)):
    sorted.append(sorted[-1]+v[i])
m = num()
for _ in range(m):
    t,l,r = arr()
    if t == 1:
        print(unsorted[r]-unsorted[l-1])
    else:
        print(sorted[r]-sorted[l-1])
