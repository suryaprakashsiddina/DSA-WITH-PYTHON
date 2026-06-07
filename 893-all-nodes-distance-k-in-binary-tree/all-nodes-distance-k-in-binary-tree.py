# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# This function builds a mapping of each node to its parent using BFS
def map_parents(root: TreeNode) -> dict:
    parent_map = {}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parent_map[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_map[node.right] = node
            queue.append(node.right)
    return parent_map

# This function performs BFS from the target node to find all nodes at distance k
def bfs_from_target(target: TreeNode, parent_map: dict, k: int) -> List[int]:
    queue = deque([target])
    visited = {target}
    current_level = 0
    while queue:
        if current_level == k:
            break
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
            if node in parent_map and parent_map[node] not in visited:
                visited.add(parent_map[node])
                queue.append(parent_map[node])
        current_level += 1
    return [node.val for node in queue]

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []
        # Step 1: Build a map of each node's parent
        parent_map = map_parents(root)
        # Step 2: Run BFS from the target node to find all nodes at distance k
        return bfs_from_target(target, parent_map, k)
        