# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        turn = True
        ans = []
        for i in a:
            if turn:
                ans.append(a[i])
                turn = False
            else:
                ans.append(a[i][::-1])
                turn = True
        return ans

