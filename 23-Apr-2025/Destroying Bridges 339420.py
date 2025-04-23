# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

###########--------Template-----------#########
from math import *
from collections import *
from random import *
from bisect import *
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
t = num()
for _ in range(t):
    n,k = arr()
    if k >= n-1:
        print(1)
    else:
        print(n)