# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = Counter(s1)
        test = Counter()
        start = 0
        for end in range(len(s2)):
            test[s2[end]]+=1
            while s <= test:
                if test==s:
                    return True
                test[s2[start]]-=1
                if not test[s2[start]]:
                    del test[s2[start]]
                start+=1
        return False
        