# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        ans = []
        while num > 0:
            if num%26 == 0:
                ans.append(26)
                num = num//26-1
                continue
            else:
                ans.append(num%26)
            num = num//26
        ans = ans[::-1]
        for i in range(len(ans)):
            ans[i] = chr(64+ans[i])
        return "".join(ans)

            
        
        