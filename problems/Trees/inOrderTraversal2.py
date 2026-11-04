from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def inOrderTraversal(self, root: Optional[TreeNode]) -> list[Optional[int]]:
		if not root:
			return []

		curr = root
		stack = []
		nodes_inorder = []

		while stack or curr:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				curr = stack.pop()
				nodes_inorder.append(curr.val)
				curr = curr.right

		return nodes_inorder
