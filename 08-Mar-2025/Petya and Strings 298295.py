# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

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
a = string()
b = string()
if a.lower() == b.lower():
    print(0)
elif a.lower() < b.lower():
    print(-1)
else:
    print(1)