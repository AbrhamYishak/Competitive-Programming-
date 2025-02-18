# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

###########--------Template-----------#########
from math import *
from collections import *
def num(): return (int(input()))
def string(): return (input())
def arr(): return list(map(int, input().split()))
def arrstr(): return list(map(str, input().split()))
###########--------Template-----------#########
n = num()
a = arr()
m = num()
b = arr()
end1 = 0
end2 = 0
sum1 = a[0]
sum2 = b[0]
count = 0
while end1 < n and end2 < m:
    while sum1 != sum2 and end1 < n and end2 < m:
        if sum1 < sum2:
            end1+=1
            if end1 < n:
                sum1+=a[end1]
        elif sum2 < sum1:
            end2+=1
            if end2 < m:
                sum2+=b[end2]
    if sum1 == sum2:
        count+=1
        end1+=1
        end2+=1
        if end1 < n and end2 < m:
            sum1=a[end1]
            sum2=b[end2]
if count < 1 or end1 != n or end2 != m:
    print(-1)
else:
    print(count)
    