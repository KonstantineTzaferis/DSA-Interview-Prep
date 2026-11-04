from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def postOrderIterative(self, root: Optional[TreeNode]) -> list[Optional[int]]:
		if not root:
			return []

		curr = root
		stack = []
		nodes_postorder = []
		last_visited = None

		while stack or curr:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				peek = stack[-1]
				if peek.right and last_visited is not peek.right:
					curr = peek.right
				else:
					nodes_postorder.append(peek.val)
					last_visited = stack.pop()

		return nodes_postorder
