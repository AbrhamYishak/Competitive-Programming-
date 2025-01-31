# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.strip().split(" ")
        return len(x[-1])
        """
        :type s: str
        :rtype: int
        """
        