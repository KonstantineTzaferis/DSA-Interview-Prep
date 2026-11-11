from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


# Returns list[int] -> The values are added in a list
class Solution:
	def inOrderTraversalRecursive(self, root: Optional[TreeNode]) -> list[int]:
		nodes = []

		def helper(root: Optional[TreeNode]):
			if not root:
				return

			helper(root.left)
			nodes.append(root.val)
			helper(root.right)

		helper(root)
		return nodes
