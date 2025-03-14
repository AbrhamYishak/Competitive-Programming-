# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        a = []
        def helper(root):
            nonlocal ans
            nonlocal a
            if root:
                a.append(str(root.val))
                if not root.left and not root.right:
                    ans.append("->".join(a))
                    return
                helper(root.left)
                if root.left:
                    a.pop() 
                helper(root.right)
                if root.right:
                    a.pop()   
        helper(root)
        return ans

        