# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flipper(arr,j):
            arr = arr[:j+1][::-1]+arr[j+1:]
            return arr
        n = len(arr)
        i = n-1
        ans = []
        while i > 0:
            j = i
            got = False
            while j >= 0 and arr[j] != n-i:
                j-=1
                got = True
            if got:
                ans.append(j+1)
                ans.append(i+1)
                arr = flipper(arr,j)
                arr = flipper(arr,i)
            i-=1
        ans.append(len(arr))
        return ans
            
        