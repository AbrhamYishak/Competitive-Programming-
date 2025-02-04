# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import *
q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = Counter(input())
    j = 0
    done = False
    for i in range(len(t)):
        if j < len(s) and s[j] == t[i]:
            j+=1
        else:
            if t[i] in p and p[t[i]] > 0:
                p[t[i]]-=1
            else:
                print("NO")
                done = True
                break
    if not done and j != len(s):
        print("NO")
        done = True
    if not done:
        print("YES")


    
    

