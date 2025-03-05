# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i],i])
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    a = stack.pop()
                    ans[a[1]]+=i-a[1]
                stack.append([temperatures[i],i])
        for i in stack:
            ans[i[1]] = 0
        return ans