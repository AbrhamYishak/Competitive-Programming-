# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []
        for i in s:
            if i!='#':
                stack_a.append(i)
            else:
                if stack_a:
                    stack_a.pop()
        for i in t:
            if i!='#':
                stack_b.append(i)
            else:
                if stack_b:
                    stack_b.pop()
        return stack_a == stack_b
