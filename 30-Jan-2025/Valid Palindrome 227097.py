# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        a = s.split(" ")
        ans = ""
        for i in a:
            for j in i:
                if j.isalnum():
                    ans+=j
        return ans.lower() == ans[::-1].lower()
        """
        :type s: str
        :rtype: bool
        """
        