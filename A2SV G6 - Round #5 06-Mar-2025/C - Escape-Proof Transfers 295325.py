# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

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
n,t,c = arr()
a = arr()
start = 0
l = defaultdict(int)
count = 0
max_val = 0
end = 0
while end < n:
    max_val  = max(max_val,a[end])
    if max_val > t:
        start = end+1
        if start < n:
            max_val =a[start]
            l = defaultdict(int)
            l[a[start]] = 1
    else:       
        l[a[end]]+=1
    if end-start+1 == c:
        count+=1
        l[a[start]]-=1
        if not l[a[start]]:
            del l[a[start]]
        start+=1
    end+=1
print(count)