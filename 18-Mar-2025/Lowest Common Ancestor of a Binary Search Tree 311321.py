# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root1 = root
        root2 = root
        def tracer(root,val,path):
            if root:
                if root.val < val:
                    path.append('right')
                    return tracer(root.right,val,path)
                elif root.val > val:
                    path.append('left')
                    return tracer(root.left,val,path)
                else:
                    return path
        path1,path2 = tracer(root1,p.val,[]),tracer(root2,q.val,[])
        for i in range(min(len(path1),len(path2))):
            if path1[i] == path2[i]:
                if path1[i] == 'left':
                    root = root.left
                else:
                    root = root.right
            else:
                return root
        return root