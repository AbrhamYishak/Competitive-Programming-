# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            a = ""
            if i == ']':
                while i == ']' and stack[-1] != '[':
                    b = ""
                    for j in stack.pop():
                        b+=j
                    a+=b[::-1]
                a = a[::-1]
                stack.pop()
                n = ""
                while stack and i == ']' and stack[-1].isdigit():
                    n+=stack.pop()
                n = n[::-1]
                stack.append(int(n)*a)
            else:
                stack.append(i)
        return "".join(stack)
