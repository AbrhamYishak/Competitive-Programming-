# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

###########--------Template-----------#########
from math import *
from collections import *
from random import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
def randomnum(): return randint(0,1)
'''
General Advice:
1, Don't Rush!
2, See the time complexity!
3, If you got wrong answer 1 or 2 times:
   1, see your code slowly!
   2, check every line of your code
      No code is clean!
   3, reread the problem!
4, If you got wrong answer 3 times change your
   approch and start from scratch!
5, don't forget xor in codeforces contests.
'''
###########--------Template-----------#########
n,k = arr()
a = arr()
b = []
for i in range(1,n):
   b.append(a[i]-a[i-1])
k = n-k
b.sort()
start = 0
ans = float("inf")
curr_sum = 0
for end in range(n-1):
   curr_sum+=b[end]
   while end-start+1 == k:
      ans = min(ans,curr_sum)
      curr_sum-=b[start]
      start+=1
if ans == float("inf"):
   print(0)
else:
   print(ans)