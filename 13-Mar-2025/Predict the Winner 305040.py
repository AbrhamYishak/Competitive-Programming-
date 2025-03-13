# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def possible(i,j,turn):
            if i > j:
                return 0
            if turn:
                turn = False
                return max(possible(i+1,j,turn)+nums[i],nums[j]+possible(i,j-1,turn))
            else:
                turn = True
                return min(-nums[i]+possible(i+1,j,turn),-nums[j]+possible(i,j-1,turn))
        return possible(0,len(nums)-1,True) >= 0

