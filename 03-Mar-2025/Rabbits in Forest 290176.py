# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = []
        a = Counter(answers)
        for i in a:
            if a[i] <= i+1:
                ans.append(i+1)
            else:
                answer = i+1
                for k in range(a[i]//(i+1)):
                    ans.append(i+1)
                if a[i]%(i+1):
                    ans.append(i+1)
        return sum(ans)
        