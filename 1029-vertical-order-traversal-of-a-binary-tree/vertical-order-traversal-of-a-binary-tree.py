# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        q = deque()
        q.append((root, 0, 0))

        while q:
            node, x, y = q.popleft()

            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            
            nodes[x][y].append(node.val)

            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))
            
        result = []

        for x in sorted(nodes.keys()):
            column = []
            for y in sorted(nodes[x].keys()):
                column.extend(sorted(nodes[x][y]))

            result.append(column)
            
        return result
            
            
        