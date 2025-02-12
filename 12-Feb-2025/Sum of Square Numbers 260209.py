# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = list(range(1,int(c**(1/2))+1))
        i = 0
        j = len(a)-1
        if (c**(1/2)) in a or c == 0:
            return True
        while i <= j:
            if a[i]**2 + a[j]**2 == c:
                return True
            elif a[i]**2 + a[j]**2 < c:
                i+=1
            else:
                j-=1
        return False