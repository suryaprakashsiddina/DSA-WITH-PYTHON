# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ks = -1

        def inorder(root, k):
            nonlocal cnt, ks
            if root:
                inorder(root.left, k)

                cnt += 1
                if cnt == k:
                    ks = root.val
                    return

                inorder(root.right, k)

        inorder(root, k)
        return ks
        