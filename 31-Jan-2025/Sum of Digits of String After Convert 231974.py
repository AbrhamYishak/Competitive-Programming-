# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution(object):
    def getLucky(self, s, k):
        num = ""
        for i in s:
            num+=str(ord(i)-96)
        while k > 0 :
            total = 0
            for i in num:
                total+=int(i)
            num = str(total)
            k-=1
        return int(num)

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        