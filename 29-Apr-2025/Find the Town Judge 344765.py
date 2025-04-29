# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {}
        for i in range(len(trust)):
            x,y = trust[i]
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)
        for i in range(1,n+1):
            if i not in graph:
                graph[i] = []
        for i in range(1,n+1):
            if i in graph and not graph[i]:
                done = True
                for j in graph.keys():
                    if i not in graph[j] and i != j:
                        done = False
                if done:
                    return i
        return -1
