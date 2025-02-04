# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        f = []
        for i in paths:
            root = i.split(" ")
            ans = []
            for k in root:
                ans.append(k.split("("))
            base = ans[0][0]
            for t in range(1,len(ans)):
                a,b = ans[t]
                b = b[:-1]
                final[b].append(base+'/'+a)
        for k in final:
            if len(final[k]) > 1:
                f.append(final[k])
        return f
