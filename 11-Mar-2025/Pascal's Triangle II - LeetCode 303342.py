# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(index):
            if index == 0:
                return [1]
            elif index == 1:
                return [1,1]
            else:
                a = [1]
                b = helper(index-1)
                for i in range(len(b)-1):
                    a.append(b[i]+b[i+1])
                a.append(1)
                return a
        return helper(rowIndex)
        