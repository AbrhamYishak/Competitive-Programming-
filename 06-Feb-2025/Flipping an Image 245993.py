# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in image:
            a = []
            for j in i:
                if j:
                    a.append(0)
                else:
                    a.append(1)
            ans.append(a[::-1])
        return ans
        