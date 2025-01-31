# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    if (arr[2] == arr[1]+arr[0]):
        print("YES")
    else:
        print("NO")