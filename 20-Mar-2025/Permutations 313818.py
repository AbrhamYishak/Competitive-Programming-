# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        choice = []
        choose = [False]*n
        def generator():
            if len(choice) == n:
                ans.append(choice.copy())
            for i in range(n):
                if choose[i]:
                    continue
                else:
                    choice.append(nums[i])
                    choose[i] = True
                    generator()
                    choice.pop()
                    choose[i] = False
        generator()
        return ans