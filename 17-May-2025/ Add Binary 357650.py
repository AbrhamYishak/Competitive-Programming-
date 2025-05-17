# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = len(a)-len(b)
        ans = []
        if l < 0:
            a = "0"*abs(l)+a
        else:
            b = "0"*abs(l)+b
        c = 0
        for i in range(len(a)-1,-1,-1):
            ans.append(str(int(a[i])^int(b[i])^c))
            c = int(a[i])&int(b[i]) | c&(int(a[i])^int(b[i]))
        if c:
            ans.append(str(c))
        return "".join(ans[::-1])


