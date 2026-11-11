from typing import Optional


class TreeNode:
	def __init__(self, val: int):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		nodes = []

		def dfs(curr):
			if not curr:
				return False

			nodes.append(curr.val)

			if dfs(root.left) or dfs(root.right):
				return True

			if sum(nodes) == targetSum and not curr.right and not curr.left:
				return True

			nodes.pop()
			return False

		return dfs(root)
