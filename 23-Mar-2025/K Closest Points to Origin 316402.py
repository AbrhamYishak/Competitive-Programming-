# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = defaultdict(list)
        ans = []
        for i in points:
            x,y = i[0],i[1]
            dis = (x**2+y**2)**(1/2)
            if dis not in distance:
                distance[dis] = [i]
            else:
                distance[dis].append(i)
        sorted_dis = dict(sorted(distance.items()))
        for i in sorted_dis:
            for j in sorted_dis[i]:
                if len(ans)!=k:
                    ans.append(j)
        return ans
        