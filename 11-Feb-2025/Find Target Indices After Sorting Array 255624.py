# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            a[nums[i]].append(i)
        return a[target]
        