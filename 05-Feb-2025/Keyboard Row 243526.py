# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr = [Counter("qwertyuiop"),Counter('asdfghjkl'),Counter('zxcvbnm')]
        ans = []
        for i in words:
            s = set(i.lower())
            for j in arr:
                if Counter(s) <= j:
                    ans.append(i)
                    break
        return ans