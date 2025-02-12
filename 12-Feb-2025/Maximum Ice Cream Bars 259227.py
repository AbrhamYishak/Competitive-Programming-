# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        nums = 0
        for i in costs:
            if coins >= i:
                coins-=i
                nums+=1
            else:
                break
        return nums
        