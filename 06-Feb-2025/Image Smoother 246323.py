# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        ans = []
        for i in range(row):
            a = []
            for j in range(col):
                sum_adjacent = 0
                num = 0
                for k in range(max(0,i-1),min(row,i+2)):
                    for l in range(max(0,j-1),min(col,j+2)):
                        sum_adjacent+=img[k][l]
                        num+=1
                a.append(sum_adjacent//num)
            ans.append(a)
        return ans
            

        