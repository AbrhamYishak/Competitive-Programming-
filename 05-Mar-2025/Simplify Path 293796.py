# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        a = path.split('/')
        for i in a:
            if i:
                if ans and i == '..':
                    ans.pop()
                elif i == '.':
                    continue
                elif i!= '..':
                    ans.append(i+'/')
        a = ('/'+"".join(ans))
        if len(a) > 1:
            return (a.rstrip('/'))
        else:
            return a

        