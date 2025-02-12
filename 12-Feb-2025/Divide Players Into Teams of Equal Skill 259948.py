# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        comp = skill[0]+skill[-1]
        ans = 0
        while i < j:
            if skill[i]+skill[j]!=comp:
                return -1 
            ans+=skill[i]*skill[j]
            i+=1
            j-=1
        return ans