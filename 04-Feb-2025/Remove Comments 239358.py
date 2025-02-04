# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        oneliner = []
        ans = []
        for i in source:
            for j in i:
                oneliner.append(j)
            oneliner.append('\n')
        multiline = False
        oneline = False
        k = 0
        while k < len(oneliner)-1:
            if oneliner[k] == '/' and oneliner[k+1] == '/':
                if not multiline:
                    oneline = True 
            elif oneliner[k] == '/' and oneliner[k+1] == '*':
                if not oneline and not multiline:
                    k+=2
                    multiline = True
                    continue
            elif oneliner[k] == "\n":
                oneline = False
            if oneliner[k] == '*' and oneliner[k+1] == '/':
                if multiline:
                    multiline = False
                    k+=2
                    continue
            if oneline == True or multiline == True:
                k+=1
                continue
            else:
                ans.append(oneliner[k])
                k+=1
        ans = "".join(ans)
        ans = ans.split("\n")
        final = []
        for i in ans:
            if i:
                final.append(i)
        return final