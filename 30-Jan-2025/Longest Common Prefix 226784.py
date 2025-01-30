# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for x in strs:
                if i >= len(x) or strs[0][i] != x[i]:
                    return strs[0][:i]
        return strs[0]
        """
        :type strs: List[str]
        :rtype: str
        """
        