# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        s = set()
        for i in strs:
            a = "".join(sorted(i))
            s.add(a)
        for i in strs:
            a = "".join(sorted(i))
            if a in s:
                d[a].append(i)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans