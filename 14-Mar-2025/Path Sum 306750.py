# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = 0
        done = False
        def helper(root,targetSum):
            nonlocal ans
            nonlocal done
            if root:
                ans+=root.val
                if not root.left and not root.right and ans == targetSum:
                    done = True
                helper(root.left,targetSum)
                helper(root.right,targetSum)
                ans-=root.val
            else:
                return 0
        helper(root,targetSum)
        return done
                