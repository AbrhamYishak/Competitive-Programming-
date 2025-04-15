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
        q.append([root,1])
        ans = defaultdict(list)
        while q:
            a = q.popleft()
            r,d = a
            if r:
                ans[d].append(r.val)
            if r and r.left:
                q.append([r.left,d+1])
            if r and r.right:
                q.append([r.right,d+1])
        final = []
        for i in ans:
            final.append(ans[i])
        return final


