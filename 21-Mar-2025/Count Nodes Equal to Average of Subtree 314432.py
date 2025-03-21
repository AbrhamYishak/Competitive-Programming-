# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def post(root):
            nonlocal ans
            if root:
                a,c_1 = post(root.right)
                b,c_2 = post(root.left)
                num = c_1+c_2+1
                if (root.val+a+b)//num == root.val:
                    ans+=1
                return (root.val+a+b,num)
            else:
                return 0, 0
        post(root)
        return ans
        