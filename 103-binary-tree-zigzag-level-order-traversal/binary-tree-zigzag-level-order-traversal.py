# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return []
        
        q = deque([root])
        LeftToRight = True

        while q:
            size = len(q)
            level = [0] * size

            for i in range(size):
                node = q.popleft()
                index = i if LeftToRight else size - 1 - i
                level[index] = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            LeftToRight = not LeftToRight
            result.append(level)
        
        return result

        