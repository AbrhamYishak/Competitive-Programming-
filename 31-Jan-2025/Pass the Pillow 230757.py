# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution(object):
    def passThePillow(self, n, time):
        right = True;
        a = 1
        while time > 0:
            time-=1
            if right:
                a+=1
            else:
                a-=1
            if a == n:
                right = False
            elif a == 1:
                right = True
        return a
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        