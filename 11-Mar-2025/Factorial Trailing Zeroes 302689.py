# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return n*factorial(n-1)
        a = factorial(n)
        ans = 0
        while not a%10:
            a//=10
            ans+=1
        return ans