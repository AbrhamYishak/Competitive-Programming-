# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        count1 = 0
        count2 = 0
        while i < j:
            if s[i]!=s[j]:
                count1+=1
                if s[i] != s[j]:
                    i+=1
            else:
                i+=1
                j-=1
        i = 0
        j = len(s)-1
        while i < j:
            if s[i]!=s[j]:
                count2+=1
                if s[i] != s[j]:
                    j-=1
            else:
                i+=1
                j-=1
        if count1 > 1 and count2> 1:
            return False
        return True