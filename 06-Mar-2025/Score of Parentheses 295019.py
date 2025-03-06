# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        ans = 0
        i = 0
        while i < (len(s)):
            if s[i] == '(':
                depth+=1
                i+=1
            else:
                if depth > 0:
                    ans+=2**(depth-1)
                while i < len(s) and s[i] == ')':
                    i+=1
                    depth-=1
        return ans

        