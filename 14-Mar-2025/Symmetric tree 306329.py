# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root1,root2):
            if root1 and root2:
                if root1.val == root2.val:
                    return True and helper(root1.left,root2.right) and helper(root1.right,root2.left)
                else:
                    return False
            else:
                if (root1 and not root2) or (not root1 and root2):
                    return False
                else:
                    return True
        return helper(root.left,root.right)

        

                
        