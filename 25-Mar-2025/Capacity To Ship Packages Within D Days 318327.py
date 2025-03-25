# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)
        def checker(m):
            sum_val = 0
            day = 1
            i = 0
            while i < len(weights):
                if sum_val+weights[i] > m:
                    day+=1
                    sum_val = 0
                else:
                    sum_val+=weights[i]
                    i+=1
            if day > days:
                return False
            return True
        while min_weight <= max_weight:
            mid = (min_weight+max_weight)//2
            if checker(mid):
                max_weight = mid-1
            else:
                min_weight = mid+1
        return min_weight