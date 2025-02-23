# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        point = arr.index(max(arr))
        count1 = 0
        count2 = 0
        i = 0
        j = 1
        while j<=point:
            if arr[i] < arr[j]:
                count1+=1
            i+=1
            j+=1
        for k in range(len(arr)-1,point,-1):
            if arr[k-1] > arr[k]:
                count2+=1 
        if len(arr) >=3 and count1+count2 == len(arr)-1 and count1!= 0 and count2!=0:
            return True
        else:
            return False
        