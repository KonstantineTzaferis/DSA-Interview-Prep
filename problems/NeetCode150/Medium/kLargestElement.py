from typing import Optional


class TreeNode:
	def __init__(self, val) -> None:
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

		stack = []
		nodes_inorder = []

		curr = root
		while stack or curr:
			while curr:
				stack.append(curr)
				curr = curr.left

			curr = stack.pop()
			nodes_inorder.append(curr.val)
			if len(nodes_inorder) == k:
				return nodes_inorder[-1]
			curr = curr.right
