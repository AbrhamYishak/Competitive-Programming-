# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in range(len(list1)):
            if list1[i] in list2:
                d[list1[i]]+=i
        for i in range(len(list2)):
            if list2[i] in list1:
                d[list2[i]]+=i
        min_val = min(d.values())
        ans = []
        for k in d:
            if d[k] == min_val:
                ans.append(k)
        return ans

        
        