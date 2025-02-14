# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 0
        j = len(cardPoints)-1
        arr = cardPoints[j-k+1:]+cardPoints[:k]
        ans = 0
        sum_nums = 0
        start = 0
        for end in range(len(arr)):
            sum_nums+=arr[end]
            if end-start+1 > k:
                sum_nums-=arr[start]
                start+=1
            ans = max(ans,sum_nums)
        return ans