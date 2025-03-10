# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def test(n):
            if n == 1:
                return True
            elif n < 1:
                return False
            n/=4
            return test(n)
        return test(n)