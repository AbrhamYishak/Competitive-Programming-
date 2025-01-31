# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        if(len(s) == len(goal)):
            return s in goal+goal
        else:
            return False
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        