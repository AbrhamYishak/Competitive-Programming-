# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        n = 0
        for i in arr:
            n = max(n,len(i))
        ans = []
        for i in range(n):
            ele = []
            for j in arr:
                if i < len(j):
                    ele.append(j[i])
                else:
                    ele.append(" ")
            ans.append("".join(ele).rstrip())
        return ans