# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        max_time = max(ranks)*pow(cars,2)
        min_time = min(ranks)
        def validate(m):
            ans = 0
            for i in ranks:
                ans+=floor(sqrt(m/i))
            return ans >= cars
        while min_time <= max_time:
            mid = (min_time+max_time)//2
            if validate(mid):
                max_time = mid-1
            else:
                min_time = mid+1
        return min_time