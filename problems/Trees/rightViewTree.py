from typing import Optional
from collections import deque


class TreeNode:
	def init(self, val: int):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def rightView(self, root: Optional[TreeNode]) -> list[Optional[int]]:
		if not root:
			return []

		queue = deque()
		nodes_right = []

		queue.append(root)

		while len(queue) > 0:
			iter_list = []
			for _ in range(len(queue)):
				curr = queue.popleft()
				iter_list.append(curr.val)

				if curr.left:
					queue.append(curr.left)

				if curr.right:
					queue.append(curr.right)

			nodes_right.append(iter_list.pop())

		return nodes_right
