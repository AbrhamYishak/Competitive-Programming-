# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i in range(len(s)):
            index[s[i]] = i
        end = index[s[0]]
        start = 0
        ans = []
        for i in range(len(s)):
            if index[s[i]] > end:
                end = index[s[i]]
            if i == end:
                ans.append(end-start+1)
                if end!=len(s)-1:
                    start = end+1
                    end = index[s[start]]
        return ans