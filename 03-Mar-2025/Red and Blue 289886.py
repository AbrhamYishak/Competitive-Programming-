# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
t = num()
for _ in range(t):
    n = num()
    r = arr()
    m = num()
    b = arr()
    for i in range(1,len(r)):
        r[i] = r[i]+r[i-1]
    for i in range(1,len(b)):
        b[i] = b[i]+b[i-1]
    print(max(0,max(r),max(b),max(r)+max(b)))
    
