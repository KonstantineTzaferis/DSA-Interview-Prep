from typing import Optional
from collections import deque


class TreeNode:
	def __init__(self, val=0):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:

		if not root:
			return []

		queue = deque()
		queue.append(root)
		nodes_bfs = []

		while len(queue) > 0:
			iter_list = []

			for _ in range(len(queue)):
				curr = queue.popleft()

				iter_list.append(curr.val)

				if curr.left:
					queue.append(curr.left)

				if curr.right:
					queue.append(curr.right)

			nodes_bfs.append(iter_list)

		return nodes_bfs


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)

s = Solution()
print(s.levelOrder(root))
