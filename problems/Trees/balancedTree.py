from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def balancedTree(self, root: Optional[TreeNode]) -> bool:

		def dfs(curr: TreeNode | None):
			if not root:
				return 0

			left = dfs(curr.left)
			right = dfs(curr.right)

			if left == -1 or right == -1:
				return -1

			if abs(left - right) > 1:
				return -1

			return 1 + max(left, right)

		return dfs(root) >= 1
