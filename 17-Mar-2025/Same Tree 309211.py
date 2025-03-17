# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if p and q:
                if p.val == q.val:
                    return True and check(p.left,q.left) and check(p.right,q.right)
                else:
                    return False
            else:
                if not p and not q:
                    return True
                else:
                    return False
        return check(p,q)

            
        