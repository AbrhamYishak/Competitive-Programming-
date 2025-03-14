# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        a = []
        ans = float("-inf")
        def helper(root):
            nonlocal a
            nonlocal ans
            if root:
                a.append(root.val)
                helper(root.left)
                if root.left:
                    a.pop()
                helper(root.right)
                if root.right:
                    a.pop()
            else:
                ans = max(ans,max(a)-min(a))
                return
        helper(root)
        return ans