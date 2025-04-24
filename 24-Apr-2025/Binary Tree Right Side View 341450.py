# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []
        q.append(root)
        while q:
            b = float("-inf")
            for i in range(len(q)):
                a = q.popleft()
                if a:
                    b = a.val
                if a and  a.left:
                    q.append(a.left)
                if a and a.right:
                    q.append(a.right)
            if b!=float("-inf"):
                ans.append(b)
        return ans