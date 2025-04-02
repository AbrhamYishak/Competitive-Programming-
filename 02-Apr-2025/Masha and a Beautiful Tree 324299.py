# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    m = num()
    a = arr()
    total_moves = 0
    def divider(a):
        global total_moves
        if len(a) == 2:
            if a[1] < a[0]:
                a[1],a[0] = a[0],a[1]
                total_moves+=1
            return a
        else:
            b = divider(a[0:(len(a))//2])
            c = divider(a[(len(a))//2:len(a)])
            if b[0] < c[0]:
                x = []
                x.extend(b)
                x.extend(c)
                return x
            else:
                x = []
                x.extend(c)
                x.extend(b)
                total_moves+=1
                return x
    if len(a) >= 2:
        if divider(a) == sorted(a):
            print(total_moves)
        else:
            print(-1)
    else:
        print(0)
            