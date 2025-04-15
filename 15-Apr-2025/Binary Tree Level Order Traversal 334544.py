# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ans = []
        while q:
            curr = []
            for _ in range(len(q)):
                a = q.popleft()
                if a:
                    curr.append(a.val)
                if  a and a.left:
                    q.append(a.left)
                if a and a.right:
                    q.append(a.right)
            if curr:
                ans.append(curr)
        return ans


