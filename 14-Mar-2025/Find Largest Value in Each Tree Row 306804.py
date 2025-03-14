# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        a = defaultdict(list)
        depth = 0
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
        ans = []
        for i in a:
            ans.append(max(a[i]))
        return ans