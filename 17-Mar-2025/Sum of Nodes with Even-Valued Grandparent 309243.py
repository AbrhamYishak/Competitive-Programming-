# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ancestors = []
        ans = 0
        def solve(root):
            nonlocal ancestors
            nonlocal ans
            if root:
                ancestors.append(root.val)
                if len(ancestors) >= 3 and not ancestors[-3]%2:
                    ans+=root.val
                solve(root.left)
                if root.left:
                    ancestors.pop()
                solve(root.right)
                if root.right:
                    ancestors.pop()
        solve(root)
        return ans

        