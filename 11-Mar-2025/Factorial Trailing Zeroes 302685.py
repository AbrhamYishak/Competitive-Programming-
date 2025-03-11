# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(0)
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return n*factorial(n-1)
        a = str(factorial(n))
        ans = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == '0':
                ans+=1
            else:
                break
        return ans