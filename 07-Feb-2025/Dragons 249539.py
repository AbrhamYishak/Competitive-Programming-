# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
s,n = arr()
dragons = []
for _ in range(n):
    dragons.append(arr())
dragons.sort(key=lambda x : x[0])
done = False
for i in dragons:
    if s <= i[0]:
        print("NO")
        done = True
        break
    else:
        s+=i[1]
if not done:
    print("YES")
