# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d[nums[i]*nums[j]].append(i)
                d[nums[i]*nums[j]].append(j)
        count = 0
        for i in d:
            if len(d[i]) >= 4:
                a = len(d[i])//2
                add = factorial(a)/(factorial(a-2)*factorial(2))
                count+=add
        return int(8*count)

        