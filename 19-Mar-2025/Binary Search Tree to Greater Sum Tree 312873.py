# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = root
        def traverse(addition,root):
            if root:
                a = traverse(addition,root.right)
                root.val += a
                if not root.right:
                    root.val+= addition
                b = traverse(root.val,root.left)
                return max(root.val,a,b)
            else:
                return 0
        traverse(0,root)
        return ans
        