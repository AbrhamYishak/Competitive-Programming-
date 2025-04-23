# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        graph = defaultdict(list)
        checker = [0]*numCourses
        ans = []
        for i in prerequisites:
            j,k = i
            graph[k].append(j)
            checker[j]+=1
        for i in range(numCourses):
            if not checker[i]:
                q.append(i)
        while q:
            a = q.popleft()
            ans.append(a)
            for i in graph[a]:
                checker[i]-=1
                if not checker[i] :
                    q.append(i)
        if len(ans) == numCourses:
            return ans
        return []