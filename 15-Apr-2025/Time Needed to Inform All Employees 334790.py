# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managers = set(manager)
        managers.remove(-1)
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        def dfs(i):
            if i in managers:
                max_l = 0
                for k in graph[i]:
                    max_l = max(max_l,dfs(k))
                return informTime[i]+max_l
            else:
                return 0
        return dfs(headID) 