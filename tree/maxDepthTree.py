# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Solution 1 (DFS)
from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        return self.maxDepthTree(root)

    def maxDepthTree(self, root):
        if root is None:
            return 0
        return max(self.maxDepthTree(root.left) + 1, self.maxDepthTree(root.right)+1)


# Solution 2 (BFS)


def maxDepth(self, root) -> int:
    if root is None:
        return 0
    queue = deque([root])
    maxDepth = 0
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        maxDepth += 1
    return maxDepth
