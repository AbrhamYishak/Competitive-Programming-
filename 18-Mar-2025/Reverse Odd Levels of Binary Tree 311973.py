# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = defaultdict(list)
        depth = 0
        root1 = root
        ans = root
        def helper(root):
            nonlocal a
            nonlocal depth
            if root:
                depth+=1
                a[depth].append(root.val)
                helper(root.left)
                if root.left:
                    depth-=1
                helper(root.right)
                if root.right:
                    depth-=1
            else:
                return
        helper(root)
        depth = 0
        def solve(root):
            nonlocal depth
            if root:
                depth+=1
                if not depth%2:
                    root.val = a[depth].pop()
                solve(root.left)
                if root.left:
                    depth-=1
                solve(root.right)
                if root.right:
                    depth-=1
            else:
                return
        solve(root1)
        return ans
