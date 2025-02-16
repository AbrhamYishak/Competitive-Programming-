# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
n = num()
ans = [0,0,0]
for _ in range(n):
    x,y,z = arr()
    ans[0]+=x
    ans[1]+=y
    ans[2]+=z
if ans == [0,0,0]:
    print("YES")
else:
    print("NO")