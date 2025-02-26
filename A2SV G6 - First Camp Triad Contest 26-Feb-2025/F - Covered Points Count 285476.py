# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

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
pre = defaultdict(int)
ans = defaultdict(int)
for _ in range(n):
    l,r = arr()
    pre[l]+=1
    pre[r+1]-=1
pre = list(sorted(pre.items(),key = lambda x: x[0]))
prefix = [x[1] for x in pre]
for i in range(1,len(prefix)):
    prefix[i] = prefix[i]+prefix[i-1]
j = 0
ans = []
final = defaultdict(int)
for i in pre:
    i = list(i)
    i[1] = prefix[j]
    ans.append(i)
    j+=1
for i in range(1,len(ans)):
    final[ans[i-1][1]] += ans[i][0] - ans[i-1][0]
if 0 in final:
    del final[0]
for l in range(1,n+1):
    if l not in final:
        final[l] = 0 
final = dict(sorted(final.items(),key = lambda x: x[0]))
final = final.values()
print(*final)