# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possible_ans = []
        a = []
        def generator(left):
            if left[0] and left[1]:
                a.append('(')
                left[0]-=1
                generator(left)               
                a.pop()
                left[0]+=1
                a.append(')')
                left[1]-=1
                generator(left)
                a.pop()
                left[1]+=1
            else:
                if left[0]:
                    a.append('(')
                    left[0]-=1
                    generator(left)
                    a.pop()
                    left[0]+=1
                    return
                elif left[1]:
                    a.append(')')
                    left[1]-=1
                    generator(left)
                    a.pop()
                    left[1]+=1
                    return
                else:
                    possible_ans.append("".join(a))
                    return
        def checker(s):
            stack = []
            for i in s:
                if not stack:
                    stack.append(i)
                else:   
                    if i == ')' and stack[-1] == '(':
                        stack.pop()  
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(i)
            if stack:
                return False
            return True
        generator([n,n])
        final_ans = []
        for i in possible_ans:
            if checker(i):
                final_ans.append(i)
        return final_ans

