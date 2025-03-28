# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        min_candies = 0
        max_candies = max(candies)
        def validate(c):
            chil = 0
            if c!=0:
                for i in candies:
                    chil+=i//c
            else:
                return True
            return chil >= k
        while min_candies <= max_candies:
            mid = (min_candies+max_candies)//2
            if validate(mid):
                min_candies = mid+1
            else:
                max_candies = mid-1
        return max_candies