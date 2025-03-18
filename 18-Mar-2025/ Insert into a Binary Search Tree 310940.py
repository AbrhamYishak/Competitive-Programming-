# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a = TreeNode(val)
        ans = root 
        def inserter(root):
            if root:
                if val > root.val and root.right:
                    inserter(root.right)
                elif val < root.val and root.left:
                    inserter(root.left)
                else:
                    if val > root.val:
                        root.right = a
                    else:
                        root.left = a
        if root:
            inserter(root)
        else:
            return a 
        return ans
         
        