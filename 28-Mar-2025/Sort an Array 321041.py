# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sorter(a):
            if len(a) == 1:
                return(a)
            else:
                b = sorter(a[:len(a)//2])
                c = sorted(a[len(a)//2:])
                i = 0
                j = 0
                ans = []
                while i < len(b) and j < len(c):
                    if b[i] < c[j]:
                        ans.append(b[i])
                        i+=1
                    else:
                        ans.append(c[j])
                        j+=1
                while i < len(b):
                    ans.append(b[i])
                    i+=1
                while j < len(c):
                    ans.append(c[j])
                    j+=1
                return ans
        return sorter(nums)
        