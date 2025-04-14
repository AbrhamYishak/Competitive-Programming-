# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        seen = set()
        def dfs(i):
            seen.add(i)
            for k in range(n):
                if k not in seen and isConnected[i][k]:
                    dfs(k)
        ans = 0
        for i in range(n):
            if i not in seen:
                ans+=1
                dfs(i)
        return ans
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        