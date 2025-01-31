# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
for _ in range(t):
    count = 0
    s = input()
    word = "codeforces"
    for i in range(10):
        if s[i]!=word[i]:
            count+=1
    print(count)