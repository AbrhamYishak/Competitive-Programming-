# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        replaced = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                replaced[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for i in range(len(nums1)):
            if nums1[i] in replaced:
                nums1[i] = replaced[nums1[i]]
            else:
                nums1[i] = -1
        return nums1

        