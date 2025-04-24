# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(root):
            if root:
                if root.left:
                    graph[root.val].append(root.left.val)
                    graph[root.left.val].append(root.val)
                    dfs(root.left)
                if root.right:
                    graph[root.val].append(root.right.val)
                    graph[root.right.val].append(root.val)
                    dfs(root.right)
        dfs(root)
        seen = set()
        q = deque()
        q.append(target.val)
        count = 0
        if count == k:
            return [target.val]
        while q:
            count+=1
            for i in range(len(q)):
                a = q.popleft()
                seen.add(a)
                for i in graph[a]:
                    if i not in seen:
                        q.append(i)
            if count == k:
                return list(q)
        return []