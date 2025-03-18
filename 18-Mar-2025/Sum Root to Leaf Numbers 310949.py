# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        ans = 0
        def checker(root):
            nonlocal path
            nonlocal ans
            if root:
                path.append(str(root.val))
                checker(root.left)
                if root.left:
                    path.pop()
                checker(root.right)
                if root.right:
                    path.pop()
                if not root.left and not root.right:
                    ans+=int("".join(path))
        checker(root)
        return ans
        