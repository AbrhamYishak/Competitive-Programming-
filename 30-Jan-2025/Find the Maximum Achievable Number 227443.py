# Problem: Find the Maximum Achievable Number - https://leetcode.com/problems/find-the-maximum-achievable-number/description/

class Solution(object):
    def theMaximumAchievableX(self, num, t):
        if (num >=0):
            return num+2*t
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        