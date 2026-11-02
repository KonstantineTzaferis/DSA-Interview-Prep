from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def inOrderTraversalIterative(self, root: Optional[TreeNode]) -> list[Optional[int]]:
		if not root:
			return []

		curr = root
		stack = []
		nodes_inorder = []

		while stack or curr:
			while curr:
				stack.append(curr)
				curr = curr.left

			curr = stack.pop()
			nodes_inorder.append(curr.val)
			curr = curr.right

		return nodes_inorder
