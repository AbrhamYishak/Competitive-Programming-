# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        num_empty = numBottles
        while num_empty >= numExchange:
            total+=num_empty//numExchange
            num_empty = num_empty//numExchange+num_empty%numExchange
        return total

        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        