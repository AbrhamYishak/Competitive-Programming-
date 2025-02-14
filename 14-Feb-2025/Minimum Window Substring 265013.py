# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        test = Counter()
        comp = float("inf")
        ans = [0,0]
        start = 0
        done = False
        for end in range(len(s)):
            test[s[end]]+=1
            while t<=test:
                if end-start+1 < comp:
                    ans = [start,end+1]
                    comp = end-start+1
                done = True
                test[s[start]]-=1
                if not test[s[start]]:
                    del test[s[start]]
                start+=1
        if not done:
            return ""
        return s[ans[0]:ans[1]]
