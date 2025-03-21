# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        max_val = 0
        n = len(words)
        letters = Counter(letters)
        ans = float("-inf")
        def checker(d,i):
            nonlocal max_val
            nonlocal ans
            if i >= n:
                return 
            a = 0
            word = Counter(words[i]) 
            dec = False
            if word <= d:
                dec = True 
                for k in words[i]:
                    d[k]-=1
                    a+=score[ord(k)-97]
            max_val+=a
            ans = max(ans,max_val)
            checker(d,i+1)
            if dec:
                d+=word
            max_val-=a
            ans = max(ans,max_val)
            checker(d,i+1)
        checker(letters,0)
        return ans

        