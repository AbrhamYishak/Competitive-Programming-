# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        reverse = False
        while n > 2:
            if k > 2**(n-1)/2:
                if reverse:
                    reverse = False
                else:
                    reverse = True
                k -= 2**(n-1)/2
            n-=1
        if k == 2:
            if reverse:
                reverse = False
            else:
                reverse = True
        if reverse:
            return 1
        return 0
