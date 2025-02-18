# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
k = num()
s = string()
def counter(n,s):
    start = 0
    count = 0
    test = [0,0]
    for end in range(len(s)):
        if s[end] == '0':
            test[0]+=1
        else:
            test[1]+=1
        while test[1] > n:
            if s[start] == '0':
                test[0]-=1
            else:
                test[1]-=1
            start+=1
        count+=end-start+1
    return count
if k!=0:
    print(counter(k,s)-counter(k-1,s))
else:
    print(counter(k,s))