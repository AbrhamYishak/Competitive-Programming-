# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            elif n%2:
                return x*helper(x,n-1)
            else:
                return helper(x*x,n//2)
        if n < 0:    
            return 1/helper(x,-n)
        else:
            return helper(x,n)
        