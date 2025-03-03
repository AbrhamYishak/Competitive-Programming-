# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0]
        for i in bills:
            if i == 5:
                change[0]+=1
            elif i == 10:
                if change[0]:
                    change[0]-=1
                    change[1]+=1
                else:
                    return False
            elif i == 20:
                if change[1] and change[0]:
                    change[1]-=1
                    change[0]-=1
                    change[2]+=1
                elif change[0] > 2:
                    change[0]-=3
                    change[2]+=1
                else:
                    return False
        return True
        