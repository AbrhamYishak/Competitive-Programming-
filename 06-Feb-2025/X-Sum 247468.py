# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
t = num()
for _ in range(t):
    max_sum = 0
    n,m = arr()
    mat = []
    for k in range(n):
        mat.append(arr())
    for i in range(n):
        for j in range(m):
            sum_diagonals = 0
            a = i
            b = j
            while a < n and b < m:
                sum_diagonals+=mat[a][b]
                a+=1
                b+=1 
            a = i
            b = j
            while a >= 0 and b >= 0:
                sum_diagonals+=mat[a][b]
                a-=1
                b-=1
            a = i
            b = j
            while a >= 0 and b < m:
                sum_diagonals+=mat[a][b]
                a-=1
                b+=1 
            a = i
            b = j
            while a < n and b >= 0:
                sum_diagonals+=mat[a][b]
                a+=1
                b-=1
            sum_diagonals-=3*(mat[i][j])
            max_sum = max(max_sum,sum_diagonals)
    print(max_sum)           