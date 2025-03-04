# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        ava = len(costs)//2
        place = [0,0]
        ans  = 0
        for i in costs:
            if i[0] > i[1]:
                if place[1] < ava:
                    place[1]+=1
                    ans+=i[1]
                else:
                    ans+=i[0]
            else:
                if place[0] < ava:
                    place[0]+=1
                    ans+=i[0]
                else:
                    ans+=i[1]
        return ans   
