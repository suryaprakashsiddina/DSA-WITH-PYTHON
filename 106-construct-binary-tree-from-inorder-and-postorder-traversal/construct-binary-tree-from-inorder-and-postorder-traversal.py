# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i

        def build(preStart, preEnd, inStart, inEnd):

            if preStart > preEnd or inStart > inEnd:
                return None

            root_val = postorder[preEnd]
            root = TreeNode(root_val)

            inRoot = in_map[root_val]

            numsLeft = inRoot - inStart

            root.left = build(
                preStart,
                preStart + numsLeft - 1,
                inStart,
                inRoot - 1
            )

            root.right = build(
                preStart + numsLeft,
                preEnd - 1,
                inRoot + 1,
                inEnd
            )

            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
        